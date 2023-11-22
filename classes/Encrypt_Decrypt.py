#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
# Instantiating a Abstract Class that requires subclass to run methods such as Encrypt and Decrypt

import os

class CaesarCipher:
    def __init__(self, key,letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        self._key = key
        self._letters = letters

    def get_key(self):
        return self._key

    def set_key(self, new_key):
        self._key = new_key

    def get_letters(self):
        return self._letters

    def transform_message(self, message, direction):
        result = ""
        for letter in message:
            if letter in self.get_letters():
                shift = self.get_key() if direction == "encrypt" else -self.get_key()
                index = (self.get_letters().find(letter) + shift) % len(self.get_letters())
                transformed_letter = self.get_letters()[index]
                if letter.isupper():
                    result += transformed_letter.upper()
                else:
                    result += transformed_letter.lower()
            else:
                result += letter
        return result

    def encrypt(self, message):
        raise NotImplementedError("Subclass / Class must implement abstract method encrypt")

    def decrypt(self, message):
        raise NotImplementedError("Subclass / Class must implement abstract method decrypt")
    @classmethod
    def brute_force_decrypt(cls, ciphertext):
        english_letter_frequencies = {
            'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.68, 'i': 7.31,
            'n': 6.95, 's': 6.28, 'r': 6.02, 'h': 5.92, 'd': 4.32,
            'l': 3.98, 'u': 2.88, 'c': 2.71, 'm': 2.61, 'f': 2.30,
            'y': 2.11, 'w': 2.09, 'g': 2.03, 'p': 1.82, 'b': 1.49,
            'v': 1.11, 'k': 0.69, 'x': 0.17, 'q': 0.11, 'j': 0.10,
            'z': 0.07
        }

        best_decryption = ""
        best_score = float('-inf')

        for key in range(26):
            instance = cls(key)
            decrypted_message = instance.transform_message(ciphertext, "decrypt")

            # Calculate the score based on letter frequencies
            score = 0
            for letter in decrypted_message:
                if letter.lower() in english_letter_frequencies:
                    score += english_letter_frequencies[letter.lower()]

            # Update the best decryption if the current score is higher
            if score > best_score:
                best_score = score
                best_decryption = decrypted_message

        print(f"Most likely plaintext: {best_decryption}")
        print(f"Probability score: {best_score}")
            
# Inherits from CaesarCipher parent class
class CaesarCipherMessage(CaesarCipher):
    def __init__(self, key):
        super().__init__(key)
        
    def encrypt(self, message):
        result = self.transform_message(message, "encrypt")
        output = f"\nPlaintext:\t{message}\nCiphertext:\t{result}"
        return output

    def decrypt(self, message):
        result = self.transform_message(message, "decrypt")
        output = f"\nCiphertext:\t{message}\nPlaintext:\t{result}"
        return output
        
# Inherits from CaesarCipher parent class     
class CaesarCipherFiles(CaesarCipher):
    
    def __init__(self, key, filename):
        super().__init__(key)
        self.filename = filename

    # Check if filename actually exists; if not, return False
    def pass_filename_criteria(self, filename):
        if os.path.exists(filename):
            return True
        else:
            return False

    # Inside CaesarCipherFiles class
    def encrypt(self,input_filename, output_filename):
        with open(input_filename, "r") as file:
            file_content = file.read()
            result = self.transform_message(file_content, "encrypt")
            with open(output_filename, "w") as output_file:
                output_file.write(result)

    def decrypt(self,input_filename, output_filename):
        with open(input_filename, "r") as file:
            file_content = file.read()
            result = self.transform_message(file_content, "decrypt")
            with open(output_filename, "w") as output_file:
                output_file.write(result)

    
#CaesarCipher.brute_force_decrypt('pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.')