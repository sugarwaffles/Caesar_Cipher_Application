from Encrypt_Decrypt import CaesarCipherFiles,CaesarCipherMessage
import os

class DictionaryAttack:
    def __init__(self, input_filename, dictionary_filename="all-words.txt"):
        self.word_set = self.import_dictionary(dictionary_filename)
        self.input_filename = input_filename
        self.caesar_cipher = CaesarCipherMessage(key=0)

    def import_dictionary(self,dictionary_filename):
        try:
            with open(dictionary_filename, 'r') as f:
                english_set = set(word.strip().lower() for word in f)
            return english_set
        except FileNotFoundError:
            print(f"Dictionary file not found: {dictionary_filename}")
            return set()

    def dictionary_attack_file(self, input_file_path):
        try:
            with open(input_file_path, 'r') as file:
                ciphertext = file.read()
        except FileNotFoundError:
            print(f"File not found: {input_file_path}")
            return None, None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None, None

        potential_results = []

        for key in range(26):
            self.caesar_cipher.set_key(key)
            decrypted_text = self.caesar_cipher.decrypt(ciphertext,format_output=False)
            print(decrypted_text,key)
            # Check for words that are common in the decrypted test are common english words
            words_in_decrypted_text = set(decrypted_text.lower().split())
            common_words = words_in_decrypted_text.intersection(self.word_set)
            print(common_words)

            if common_words:
                potential_results.append((decrypted_text, key, common_words))

        if not potential_results:
            return None, None
        #Scoring to select the result with highest count of common english words
        best_result = max(potential_results, key=lambda x: len(x[2]))
        return best_result[0], best_result[1]
    

# Example usage:
dictionary_attack_instance = DictionaryAttack(input_filename="Dataset/asdasd.txt", dictionary_filename="Dataset/words.txt")
file_path = os.path.join("Dataset", "asdasd.txt")
decrypted_text, key = dictionary_attack_instance.dictionary_attack_file(file_path)

if decrypted_text is not None:
    print(f"Results:\n{decrypted_text}")
    print(f"\nKey: {key}")
else:
    print("Decryption unsuccessful.")