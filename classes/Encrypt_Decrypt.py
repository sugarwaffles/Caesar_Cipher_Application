
class CaesarCipher:

    def __init__(self, key):
        self.key = key
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def get_cipherletter(self, new_key, letter):
        if letter in self.letters:
            if letter.isupper():
                return self.letters[new_key].upper()
            else:
                return self.letters[new_key].lower()
        else:
            return letter

    def encrypt(self, message):
        result = ""
        for letter in message:
            new_key = (self.letters.find(letter) + self.key) % len(self.letters)
            result = result + self.get_cipherletter(new_key, letter)
        
        # Display and format both plaintext and ciphertext     
        Output = f"\nPlaintext:\t{message}\nCiphertext:\t{result}"
            
        return Output

    def decrypt(self, message):
        result = ""
        for letter in message:
            new_key = (self.letters.find(letter) - self.key) % len(self.letters)
            result = result + self.get_cipherletter(new_key, letter)
            
        # Display and format both plaintext and ciphertext    
        Output = f"\nCiphertext:\t{result}\nPlaintext:\t{message} "
            
        return Output



# Caesar Cipher child class for messages
class CaesarCipherMessage(CaesarCipher):
    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, text):
        super().encrypt(text)

    def decrypt(self, text):
        super().decrypt(text)

# Caesar Cipher child class for files
class CaesarCipherFile(CaesarCipher):
    def __init__(self, key, filename):
        super().__init__(key)
        self.filename = filename

    def encrypt_file(self):
        pass

    def decrypt_file(self):
        pass
