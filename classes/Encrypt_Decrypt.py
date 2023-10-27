
class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def transform_message(self, message, direction):
        result = ""
        for letter in message:
            if letter in self.letters:
                shift = self.key if direction == "encrypt" else -self.key
                index = (self.letters.find(letter) + shift) % len(self.letters)
                transformed_letter = self.letters[index]
                if letter.isupper():
                    result += transformed_letter.upper()
                else:
                    result += transformed_letter.lower()
            else:
                result += letter
        return result

    def encrypt(self, message):
        result = self.transform_message(message, "encrypt")
        output = f"\nPlaintext:\t{message}\nCiphertext:\t{result}"
        return output

    def decrypt(self, message):
        result = self.transform_message(message, "decrypt")
        output = f"\nCiphertext:\t{message}\nPlaintext:\t{result}"
        return output
    
    def encrypt_file(self,filename,output_filename):
        file = open(f"Dataset/{filename}","r")
        file_content = file.read()
        result = self.transform_message(file_content, "encrypt")
        
        # write mode to allow creating if file does not exist /overwriting a file if already exist 
        with open(f"Dataset/{output_filename}","w") as output_file:
            output_file.write(result)
            
    def decrypt_file(self,filename,output_filename):
        file = open(f"Dataset/{filename}","r")
        file_content = file.read()
        result = self.transform_message(file_content, "decrypt")
        
        # write mode to allow creating if file does not exist /overwriting a file if already exist 
        with open(f"Dataset/{output_filename}","w") as output_file:
            output_file.write(result)
            
        
        
        

# Caesar Cipher child class for files
class CaesarCipherFile(CaesarCipher):
    def __init__(self, key, filename):
        super().__init__(key)
        self.filename = filename

    def encrypt_file(self):
        pass

    def decrypt_file(self):
        pass
