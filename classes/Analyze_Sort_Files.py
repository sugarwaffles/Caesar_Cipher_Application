#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
from classes.Letter_Dist import LetterNode,Node,SortedList
from classes.Infer_Cipher import BreakCaesarCipher
from classes.Encrypt_Decrypt import CaesarCipherFiles
from classes.Cipher_Handler import CipherHandler
import os
class CipherNode(Node):
    def __lt__(self, other):
        # Customize the comparison logic for sorting CipherNodes
        return self.data[1] < other.data[1] or (self.data[1] == other.data[1] and self.data[0] < other.data[0])


class AnalyzeSortFiles:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.__reference_file = os.path.join(os.path.dirname(__file__), "..", "Dataset", "englishtext.txt")
    
    def get_reference_file(self):
        return self.__reference_file

    def analyze_and_sort_files(self):
        encrypted_files = [f for f in os.listdir(self.folder_path) if f.endswith('.txt')]

        if not encrypted_files:
            print(f"No encrypted files found in the folder '{self.folder_path}'.")
            return

        # Sort files by name to ensure they are processed in the correct order
        encrypted_files.sort()

        # Create an empty SortedList instance with CipherNode
        sorted_list = SortedList()

        # Decrypt each file and generate output files
        for i, encrypted_file in enumerate(encrypted_files):
            input_path = os.path.join(self.folder_path, encrypted_file)

            cipher_breaker = BreakCaesarCipher(input_path)
            cipher_breaker.reference_file_analysis(self.get_reference_file())

            # Calculate Cipher Key
            cipher_key = cipher_breaker.calculate_cipher_key()

            # Append the file name and inferred key to the SortedList using CipherNode
            sorted_list.insert(CipherNode([encrypted_file, cipher_key]))

        # Get the sorted list
        sorted_files = sorted_list.get_sorted_list()

        #Log storage using list
        log = []
        
        # Print the sorted files & store each line in the log 
        for i, file_info in enumerate(sorted_files.items()):
            file_name, cipher_key = file_info
            output_file = f"file{i + 1}.txt"
            log_line = f"Decrypting: {file_name} with key {cipher_key} as: {output_file}"
            log.append(log_line)
            print(f"\n{log_line}")
            
            # Decrypt the file and generate the output file using CipherHandler
            CipherHandler.decrypt_file(cipherkey=cipher_key, input_path=(os.path.join(self.folder_path, file_name)), output_file=output_file)
        
        # Write the logs to a file
        
        log_file_path = os.path.join(self.folder_path, "log.txt")
        with open(log_file_path, "w") as log_file:
            log_file.write("\n".join(log))
