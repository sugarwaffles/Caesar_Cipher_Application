# Name: Wilfred Djumin
# Class: DAAA/FT/2B05
# Instantiating a Abstract Class that requires subclass to run methods such as Encrypt and Decrypt

import os
import string


class CaesarCipher:
    def __init__(self, key, letters=string.ascii_letters):
        self.__key = key
        self.__letters = letters
    # Getter and setter methods for key and letters

    def get_key(self):
        return self.__key

    def set_key(self, new_key):
        self.__key = new_key

    def get_letters(self):
        return self.__letters

# Transform the given message based on the specified direction (encrypt or decrypt)


    def transform_message(self, message, direction):
        result = ""
        
        # Iterate through each letter in the message
        for letter in message:
            # Check if the letter is in the allowed letters set
            if letter in self.get_letters():
                # Determine the shift direction based on the action (encrypt or decrypt)
                shift = self.get_key() if direction == "encrypt" else -self.get_key()
                
                # Calculate the new index after applying the shift
                index = (self.get_letters().find(letter) +
                        shift) % len(self.get_letters())

                # Get the transformed letter at the new index
                transformed_letter = self.get_letters()[index]

                # Append the transformed letter to the result, maintaining the case
                result += transformed_letter.upper() if letter.isupper() else transformed_letter.lower()
            else:
                # If the letter is not in the allowed letters set, append it unchanged to the result
                result += letter

        # Return the final transformed result
        return result

    # Abstract methods for encrypt and decrypt to be implemented by subclasses

    def encrypt(self, message):
        raise NotImplementedError(
            "Subclass / Class must implement abstract method encrypt")

    def decrypt(self, message):
        raise NotImplementedError(
            "Subclass / Class must implement abstract method decrypt")

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
            decrypted_message = instance.transform_message(
                ciphertext, "decrypt")
            print(decrypted_message)
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
    # Inherit the encrypt/decrypt method from parent class
    def transform_message(self, message, direction, format_output=True):
        result = super().transform_message(message, direction)
        if format_output:
            # Format output if wish to
            return self.format_output(message, result, direction)
        else:
            return result
    # Format the output after decryption / encryption

    def format_output(self, message, result, transformation):
        if transformation == 'encrypt':
            return f"\nPlaintext:\t{message}\nCiphertext:\t{result}"
        else:
            return f"\nCiphertext:\t{message}\nPlaintext:\t{result}"

# Inherits from CaesarCipher parent class


class CaesarCipherFiles(CaesarCipher):
    def __init__(self, key, filename):
        super().__init__(key)
        self.__filename = filename

    def get_filename(self):
        return self.__filename

    def encrypt_or_decrypt_file(self, input_filename, output_filename, operation):
        # First read the file and decrypt / encrypt depending on operation
        with open(input_filename, "r") as file:
            file_content = file.read()
            # Pass the correct transformation direction to transform_message
            result = self.transform_message(file_content, operation)
            # Then write the results to output file, overwrite if file exists
            with open(output_filename, "w") as output_file:
                output_file.write(result)
                
