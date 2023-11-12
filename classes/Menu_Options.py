import os
from classes.Encrypt_Decrypt import CaesarCipher,CaesarCipherMessage,CaesarCipherFiles
from classes.Letter_Dist import LetterFrequencyDistribution
class MenuOptions:
    def __init__(self):
        
        #dictionary storing options from 1 - 8 
        self.menu_options = {
            1: 'Encrypt/Decrypt Message',
            2: 'Encrypt/Decrypt File',
            3: 'Analyze letter frequency distribution',
            4: 'Infer Caesar cipher key from file',
            5: 'Analyze and sort encrypted files',
            6: 'Extra Option One',
            7: 'Extra Option Two',
            8: 'Exit'
        }
    # prevents users from just pressing "Enter" for certain inputs
    def get_non_empty_input(self, prompt):
        user_input = input(prompt)
        while not user_input.strip():  # Check if the input is empty or contains only whitespace
            print("Input cannot be empty. Please try again.")
            user_input = input(prompt)
        return user_input
    
    def start(self):
        # print essential introduction 
        print('\n***********************************************************************')
        print('* ST1507 DSAA: Welcome To:                                            *')
        print('*                                                                     *')
        print('*  ~ Caesar Cipher Encrypted Message Analyzer ~                       *')
        print('*---------------------------------------------------------------------*')
        print('*                                                                     *')
        print('*  - Done By: Wilfred Djumin (2237503)                                *')
        print('*  - Class DAAA/FT/2B/05                                              *')
        print('*********************************************************************** \n')
        # Prompt user to press "Enter" key 
        starting_input = input("Press Enter to continue...")
        # Prompt user to press "Enter" key 
        
        
    def print_menu(self):
        print("\nPlease select your choice: (1,2,3,4,5,6,7,8)")
        #Looping through dictionary to list options to user
        for choice, description in self.menu_options.items():
            print(f"\t {choice}. {description}")

    def get_choice(self):
        
        #reference: https://python-course.eu/python-tutorial/errors-and-exception-handling.php
        
        while True:
            
            try:
                
                # Prompt user for choice 
                choice = int(input("Enter your choice: "))
                
                # Check if the choice exist in the menu_options dictionary
                if choice in self.menu_options:
                    
                    
                    #Ask user for confirmation 
                    confirm_choice = input(f'You chose option {choice}: {self.menu_options.get(choice)}. Confirm? (y/n): ').lower()
                    
                    if confirm_choice == 'y':
                    # Return the inputted choice if confirmed
                        return choice
                    elif confirm_choice == 'n':
                        print('Operation canceled. Please choose again.\n')
                    else:
                        print('Invalid confirmation. Please enter "y" for yes or "n" for no.\n')
  
                # If not, prompt user to re-enter a number between 1 and 8
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.\n")
                    
            #raise ValueError if user does not input a number/integer     
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                
    # method/function that filters what function(s) to run based on user input
    def handle_choice(self, choice):
        if choice == 1:
            self.handle_encryption_decryption('message')
        elif choice == 2:
            self.handle_encryption_decryption('file')
        elif choice == 3:
            self.analyze_letter_frequency()
        elif choice == 4:
            self.infer_caesar_cipher_key()
        elif choice == 5:
            self.analyze_encrypted_files()
        elif choice == 6:
            self.extra_option_one()
        elif choice == 7:
            self.extra_option_two()
        elif choice == 8:
            #Execute a clean exit if user presses 8
            print("Bye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer")
            exit(0)       
            
    def get_valid_cipherkey(self):
     while True:
        try:
            cipherkey = int(input("\nEnter the cipher key: "))
            return cipherkey
        except ValueError:
            print("Please enter a valid number.")
                     
    def handle_encryption_decryption(self, input_type):
        while True:
            action = ''
            # Prompt the user to select either encryption or decryption
            while action != "e" and action != 'd':
                action = input('\nEnter "E" for Encrypt or "D" for Decrypt: ').lower()
                if action != "e" and action != 'd':
                    print("Only enter either 'E' or 'D'")
                
            if action == "e":
                
                # Get the plaintext input to be encrypted
                plaintext = self.get_non_empty_input(f"\nPlease type {input_type} you want to encrypt: ")
                
                # Check if the input type is a file and check if it exists
                if input_type == 'file':
                    if not os.path.exists(f"Dataset\{plaintext}"):
                        print(f"File {plaintext} not found.")
                        break
                    
                    # Get the encryption key and instantiate the cipher class files
                    cipherkey = self.get_valid_cipherkey()
                    cipher = CaesarCipherFiles(cipherkey, plaintext)
                    output_file = self.get_non_empty_input("\nPlease enter an output file: ")
                    
                    # Encrypt the file and show results in a new txt file
                    cipher.encrypt(plaintext, output_file)
                else:
                    # Get the encryption key and instantiate the cipher class message
                    cipherkey = self.get_valid_cipherkey()
                    cipher = CaesarCipherMessage(cipherkey)
                    # Encrypt the message and show results
                    print(cipher.encrypt(plaintext))
                    
                # If the encryption is successful, break the loop and return to the initial selection menu
                break
                
            elif action == 'd':
                
                # Get the ciphertext input to be decrypted
                ciphertext = self.get_non_empty_input(f"\nPlease type {input_type} you want to decrypt: ")
                
                # Check if the input type is a file and check if it exists
                if input_type == 'file':
                    if not os.path.exists(f"Dataset\{ciphertext}"):
                        print(f"File {ciphertext} not found.")
                        break
                    
                    # Get the decryption key and instantiate the appropriate cipher class for files
                    cipherkey = self.get_valid_cipherkey()
                    cipher = CaesarCipherFiles(cipherkey, ciphertext)
                    output_file = self.get_non_empty_input("\nPlease enter an output file: ")
                    # Decrypt the file and save results to the output file
                    cipher.decrypt(ciphertext, output_file)
                    
                else:
                    # Get the decryption key and instantiate the appropriate cipher class for message
                    cipherkey = self.get_valid_cipherkey()
                    cipher = CaesarCipherMessage(cipherkey)
                    # Decrypt the message and display the result
                    print(cipher.decrypt(ciphertext))
                    
                # If the decryption is successful, break the loop and return to the initial selection menu
                break


                
    def analyze_letter_frequency(self):
        # Instantiate the LetterFrequencyDistribution class and prompt user for file 
        letter_dist_input = input("Please enter the file you want to analyze: ")
        
        #Check file path if it exists
        file_path = os.path.join(os.path.dirname(__file__), "..", "Dataset", letter_dist_input)
        
        if os.path.exists(file_path):
            letter_dist = LetterFrequencyDistribution(file_path)
            # Call the analyze_file method here if needed
            letter_dist.analyze_file()
            # Call other methods or operations as needed
        else:
            print(f'File not found: {letter_dist_input}')      

        input("\nPress enter key, to continue.....")