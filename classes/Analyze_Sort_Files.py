#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
from classes.Letter_Dist import LetterNode
from classes.Letter_Dist import SortedList
from classes.Infer_Cipher import breakCaesarCipher
from classes.Encrypt_Decrypt import CaesarCipherFiles
from classes.CipherHandler import CipherHandler
import os

class AnalyzeSortFiles:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.__reference_file = os.path.join(os.path.dirname(__file__), "..", "Dataset", "englishtext.txt")
    
    def get_reference_file(self):
        return self.__reference_file
    
    # Reusing the logic from our MenuOptions.py
    def decrypt_file(self, cipherkey, input_path, output_file):
        output_file_path = self.create_output_file(output_file)
        if output_file_path is not None:
            cipher = CaesarCipherFiles(cipherkey, input_path)
            cipher.decrypt(input_path, output_file_path)

    def analyze_and_sort_files(self):
        encrypted_files = [f for f in os.listdir(self.folder_path) if f.endswith('.txt')]

        if not encrypted_files:
            print(f"No encrypted files found in the folder '{self.folder_path}'.")
            return

        # Sort files by name to ensure they are processed in the correct order
        encrypted_files.sort()

        # Create an empty SortedList instance
        sorted_list = SortedList()

        # Decrypt each file and generate output files
        for i, encrypted_file in enumerate(encrypted_files):
            input_path = os.path.join(self.folder_path, encrypted_file)

            cipher_breaker = breakCaesarCipher(input_path)
            cipher_breaker.reference_file_analysis(self.get_reference_file())

            # Calculate Cipher Key
            cipher_key = cipher_breaker.calculate_cipher_key()

            # Append the file name and inferred key to the SortedList
            sorted_list.insert(LetterNode([encrypted_file, cipher_key]))

        # Get the sorted list
        sorted_files = sorted_list.get_sorted_list()
        
        # Print the sorted files
        for i, (file_name, cipher_key) in enumerate(sorted_files):
            output_file = f"file{i + 1}.txt"
            print(f"\nDecrypting: {file_name} with key {cipher_key} as: file{i + 1}.txt")
            
            # Decrypt the file and generate the output file using CipherHandler
            CipherHandler.decrypt_file( cipherkey=cipher_key,input_path = (os.path.join(self.folder_path, file_name)),output_file=output_file)

        #print("Batch decryption completed successfully.")
