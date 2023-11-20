import os
import string
from classes.Encrypt_Decrypt import CaesarCipherFiles,CaesarCipherMessage

class CipherHandler:
    def __init__(self):

        pass

    @staticmethod
    def create_output_file(output_filename):
        # Ensure the "Dataset" directory exists
        dataset_dir = os.path.join(os.path.dirname(__file__), "..", "Dataset")
        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir)

        # Check if the output filename has a .txt extension
        if not output_filename.lower().endswith(".txt"):
            print("Output filename must end with '.txt'")
            return None  # Return None if the filename doesn't end with .txt

        # Normalize the output filename to handle invalid characters
        normalized_output_filename = os.path.normpath(output_filename)

        # Remove invalid characters from the file name
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        sanitized_output_filename = ''.join(c for c in normalized_output_filename if c in valid_chars)

        # Split the sanitized output_filename into directory and file name components
        output_dir, output_file = os.path.split(sanitized_output_filename)

        # Create the full path for the output file in the "Dataset" directory
        return os.path.join(dataset_dir, output_file)
    
    @staticmethod
    def get_cipher_instance(cipherkey, input_type, filename=None):
        if input_type == 'message':
            return CaesarCipherMessage(cipherkey)
        elif input_type == 'file':
            if filename is not None:
                return CaesarCipherFiles(cipherkey, filename)
            else:
                # Handle the case where filename is None or not provided
                return None
        else:
            # Handle other input types if needed
            return None

    
    @staticmethod
    def encrypt_file(cipherkey, input_path, output_file):
        output_file_path = CipherHandler.create_output_file(output_file)
        if output_file_path is not None:
            cipher = CaesarCipherFiles(cipherkey, input_path)
            cipher.encrypt(input_path, output_file_path)

    @staticmethod
    def decrypt_file(cipherkey, input_path, output_file):
        output_file_path = CipherHandler.create_output_file(output_file)
        if output_file_path is not None:
            cipher = CaesarCipherFiles(cipherkey, input_path)
            cipher.decrypt(input_path, output_file_path)