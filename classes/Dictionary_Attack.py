from classes.Encrypt_Decrypt import CaesarCipherFiles,CaesarCipherMessage
from classes.Input_Handler import InputHandler
import os
# This class represents a Pure Brute Force Attack using a Caesar Cipher.
class PureBruteForceAttack:
    # Constructor method to initialize the attack with an input filename.
    def __init__(self, input_filename):
        # Initialize a Caesar Cipher with a default key of 0.
        self.caesar_cipher = CaesarCipherMessage(key=0)
        # Store the input filename for later use.
        self.input_filename = input_filename

    # Read the ciphertext from the specified input file.
    def read_ciphertext(self):
        try:
            with open(self.input_filename, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            print(f"File not found: {self.input_filename}")
            raise e
        except Exception as e:
            print(f"Error reading file: {e}")
            raise e

    # Perform a brute force attack to decrypt the ciphertext.
    def perform_attack(self):
        # Initialize a list to store potential decryption results.
        potential_results = []
        # Read the ciphertext from the file.
        ciphertext = self.read_ciphertext()

        # If the ciphertext is not available, return None.
        if ciphertext is None:
            return None, None

        # Iterate through all possible keys (0 to 25).
        for key in range(26):
            self.caesar_cipher.set_key(key)
            decrypted_text = self.caesar_cipher.decrypt(ciphertext, format_output=False)
            potential_results.append((decrypted_text, key, set()))

        # Select the result with the highest count of common English words.
        best_result = max(potential_results, key=lambda x: len(x[2]))
        return best_result, potential_results

    # Write the results of the attack to an output file.
    def write_results_to_file(self, output_file_path=None, best_result=None, all_results=None):
        # Create the output file path using the static method from Input_Handler.
        output_file_path = InputHandler.create_output_file(output_file_path or "output.txt")
        with open(output_file_path, 'w') as output_file:
            # Write the encrypted text to the output file.
            output_file.write(f"Encrypted Text:\n{self.read_ciphertext()}\n")
            # Write each decrypted text with its corresponding key.
            for decrypted_text, key, _ in all_results:
                output_file.write(f"\nDecrypted Text( Key: {key} ):\n{decrypted_text}\n")


# This class represents a Dictionary Attack, inheriting from PureBruteForceAttack.
class DictionaryAttack(PureBruteForceAttack):
    # Constructor method to initialize the attack with an input filename and optional dictionary filename.
    def __init__(self, input_filename, dictionary_filename="all-words.txt"):
        # Call the constructor of the parent class.
        super().__init__(input_filename)
        # Import the dictionary words and store them in a set.
        self.word_set = self.import_dictionary(dictionary_filename)

    # Import the dictionary words from a file and return a set.
    def import_dictionary(self, dictionary_filename):
        try:
            with open(dictionary_filename, 'r') as f:
                return set(word.strip().lower() for word in f)
        except FileNotFoundError as e:
            print(f"Dictionary file not found: {dictionary_filename}")
            raise e

    # Perform a dictionary attack using the imported dictionary.
    def dictionary_attack_file(self, input_file_path, output_file=None, use_dictionary=True):
        try:
            # Read the ciphertext from the input file using the parent class method.
            ciphertext = super().read_ciphertext()
        except FileNotFoundError as e:
            print(f"File not found: {input_file_path}")
            raise e

        # Perform the brute force attack to generate potential results.
        best_result, all_results = self.perform_attack()

        # Filter potential results based on the use of the dictionary.
        if use_dictionary:
            potential_results = [(result[0], result[1], set(result[0].lower().split()) & self.word_set) for result in all_results]
        else:
            potential_results = [(result[0], result[1], set()) for result in all_results]

        # If there are no potential results, return None.
        if not potential_results:
            return None, None

        # Select the result with the highest count of common English words.
        best_result = max(potential_results, key=lambda x: len(x[2]))

        # Call the overridden method to write the results to an output file.
        self.write_results_to_file(output_file_path=output_file, best_result=best_result, all_results=potential_results)

        return best_result[0], best_result[1]

    # Override the parent class method to provide custom behavior for writing results to a file.
    def write_results_to_file(self, output_file_path=None, best_result=None, all_results=None):
        # Create the output file path using the static method from Input_Handler.
        output_file_path = InputHandler.create_output_file(output_file_path or "output.txt")
        # Override the method to provide custom behavior for writing results to a file.
        with open(output_file_path, 'w') as output_file:
            # Write the first decrypted text to the output file (assuming you want the first one).
            output_file.write(f"Encrypted Text:\n{all_results[0][0]}\n")
            output_file.write(f"\nDecrypted Text:\n{best_result[0]} , Key: {best_result[1]}\n")