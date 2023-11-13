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
        if self.pass_filename_criteria(filename) == True:
            super().__init__(key)
            self._filename = filename
        else:
            print("Filename does not exist! ")

    # Check if filename actually exists; if not, return False
    def pass_filename_criteria(self, filename):
        if os.path.exists(filename):
            return True
        else:
            return False

    def encrypt(self, filename, output_filename):
        with open(filename, "r") as file:
            file_content = file.read()
            result = self.transform_message(file_content, "encrypt")
            with open(output_filename, "w") as output_file:
                output_file.write(result)

    def decrypt(self, filename, output_filename):
        with open(filename, "r") as file:
            file_content = file.read()
            result = self.transform_message(file_content, "decrypt")
            with open(output_filename, "w") as output_file:
                output_file.write(result)

                