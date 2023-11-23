
#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
from classes.Encrypt_Decrypt import CaesarCipherFiles,CaesarCipherMessage
from classes.Input_Handler import InputHandler

# Inherits from Input Handler 


class CipherHandler(InputHandler):
    # Option 1 & 2 user input error handling
    def get_action_input(self):
        action = ''
        #Keep prompting user
        while action not in ('e', 'd'):
            action = input('\nEnter "E" for Encrypt or "D" for Decrypt: ').lower()
            if action not in ('e', 'd'):
                print("Only enter either 'E' or 'D'")
        # Return back the full string based on user input e for encrypt, d for decrypt
        full_action = 'encrypt' if action == 'e' else 'decrypt'
        return full_action

    def get_valid_cipherkey(self):
        while True:
            try:
                cipherkey = int(input("\nEnter the cipher key: "))
                return cipherkey
            except ValueError:
                print("Please enter a valid number.")

    def get_cipher_instance(self, cipherkey, input_type, filename=None):
        
        if input_type == 'message':
            return CaesarCipherMessage(cipherkey)
        elif input_type == 'file':
            if filename:
                return CaesarCipherFiles(cipherkey, filename)
            else:
                print("Filename not provided. Cannot create Cipher instance.")
        else:
            print(f"Invalid input type: {input_type}. Cannot create Cipher instance.")
                
    def process_file(self, cipherkey, input_path, output_file, operation):
            output_file_path = super().create_output_file(output_file)
            if output_file_path:
                try:
                    cipher = self.get_cipher_instance(cipherkey, 'file', input_path)
                    # Pass the correct transformation direction to process_file
                    cipher.encrypt_or_decrypt_file(input_path, output_file_path, operation)
                except Exception as e:
                    print(f"Error during {operation}: {e}")