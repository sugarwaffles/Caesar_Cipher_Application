#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
from classes.Letter_Dist import LetterNode,Node,SortedList
from classes.Infer_Cipher import BreakCaesarCipher
from classes.Encrypt_Decrypt import CaesarCipherFiles
from classes.Cipher_Handler import CipherHandler
import os

#Child of the Node class 
class CipherNode(Node):
    def __lt__(self, other):
        # Customize the comparison logic for sorting CipherNodes
        return self.data[1] < other.data[1] or (self.data[1] == other.data[1] and self.data[0] < other.data[0])


class AnalyzeSortFiles:
    def __init__(self, folder_path):
        self.cipher_handler = CipherHandler()
        self.__folder_path = folder_path
        self.__reference_file = self.find_reference_file()
        
    def find_reference_file(self):
        reference_file_path = os.path.join(os.path.dirname(__file__), "..", "Dataset", "englishtext.txt")

        if os.path.exists(reference_file_path):
            return reference_file_path
        else:
            print(f"Warning: Reference file 'englishtext.txt' not found.")
            return None
        
    def get_reference_file(self):
        return self.__reference_file
    def get_folder_path(self):
        return self.__folder_path
    def analyze_and_sort_files(self):
        # Check if the reference file is available before proceeding
        if self.get_reference_file() is None:
            print("Cannot proceed with analysis. Reference file not found.")
            return None
        # Retrieve potential encrypted files from the folder with .txt
        encrypted_files = [file for file in os.listdir(self.get_folder_path()) if file.endswith('.txt')]

        if not encrypted_files:
            print(f"No encrypted files found in the folder '{self.get_folder_path()}'.")
            return None

        # Sort files by name to ensure they are processed in the correct order
        encrypted_files.sort()

        # Create an empty SortedList instance with CipherNode
        sorted_list = SortedList()

        # Decrypt each file and generate output files
        for i, encrypted_file in enumerate(encrypted_files):
            input_path = os.path.join(self.get_folder_path(), encrypted_file)

            cipher_breaker = BreakCaesarCipher(input_path)
            cipher_breaker.reference_file_analysis(self.get_reference_file())

            # Calculate Cipher Key
            cipher_key = cipher_breaker.calculate_cipher_key()
            # Check if the current file is the reference file
            if encrypted_file == os.path.basename(self.get_reference_file()):
                print(f"\nSkipping decryption for reference file: {encrypted_file}")
                continue
            # Skip decryption if the key is 0
            elif cipher_key == 0:
                print(f"\nSkipping decryption for {encrypted_file} as the inferred key is 0.")
                continue
            # Do not decrypt the log file 
            elif encrypted_file.startswith("log"):
                continue
            # Append the file name and inferred key to the SortedList using CipherNode
            sorted_list.insert(CipherNode([encrypted_file, cipher_key]))
        print("")
        # Get the sorted list
        sorted_files = sorted_list.get_sorted_list()

        # Log storage using list
        log = []

        # Print the sorted files & store each line in the log
        for i, file_info in enumerate(sorted_files.items()):
            file_name, cipher_key = file_info
            output_file = f"file{i + 1}.txt"
            log_line = f"Decrypting: {file_name} with key {cipher_key} as: {output_file}\n"
            log.append(log_line)
            print(log_line)

            # Decrypt the file and generate the output file using CipherHandler
            self.cipher_handler.process_file(cipherkey=cipher_key, input_path=(os.path.join(self.get_folder_path(), file_name)), output_file=output_file,operation='decrypt')

        # Write the logs to a file
        log_file_path = os.path.join(self.get_folder_path(), "log.txt")
        with open(log_file_path, "a+") as log_file:
            # Add a newline character before appending the new content
            log_file.write("\n")
            log_file.write("".join(log))
            
