import os
from classes.Encrypt_Decrypt import CaesarCipher
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
                    #accepts and returns the inputted choice
                    return choice
                
                # If not, prompt user to re-enter a number between 1 and 8
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.")
                    
            #raise ValueError if user does not input a number/integer     
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
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
                     
    def handle_encryption_decryption(self,input_type):
            action = ''
            
            # Continuously prompt the user until valid input is provided "E" or "D" (case sensitive) 
            while action != "E" and action != 'D':
                action = input('\nEnter "E" for Encrypt or "D" for Decrypt: ')
                
                # Display error message if the input is not E or D
                if action != "E" and action != 'D':
                    print("Only enter either 'E' or 'D' (case sensitive)")
            
            # Encrypt or decrypt based on the user's action/input
            if action == "E":
                
                plaintext = self.get_non_empty_input(f"\nPlease type {input_type} you want to encrypt: ")
                
                # If user selected Encrypt file, we check file path if exist, if not re-input the filename  
                while input_type == 'file' and not os.path.exists(f"Dataset\{plaintext}"):
                    print(f"File {plaintext} not found.")
                    plaintext = self.get_non_empty_input(f"\nPlease type {input_type} you want to encrypt: ")
                            
                cipherkey = self.get_valid_cipherkey()
                    
                if input_type == 'file':
                    output_file = self.get_non_empty_input("\nPlease enter a output file: ")
                    
                    
                #Instantiate a CaesarCipher class with the inputted cipher key 
                cipher = CaesarCipher(cipherkey)
                
                if input_type == 'message':
                    #Calling the encrypt method 
                    print(cipher.encrypt(plaintext))
                else:
                    print(cipher.encrypt_file(plaintext,output_file))
            
            
            elif action == 'D':
                ciphertext = self.get_non_empty_input(f"\nPlease type {input_type} you want to decrypt: ")
                
                # If user selected Decrypt file, we check file path if exist, if not re-input the filename  
                while input_type == 'file' and not os.path.exists(f"Dataset\{ciphertext}"):
                    print(f"File {ciphertext} not found.")
                    ciphertext = self.get_non_empty_input(f"\nPlease type {input_type} you want to encrypt: ")
                    
                cipherkey = self.get_valid_cipherkey()
    
                if input_type == 'file':
                    output_file = self.get_non_empty_input("\nPlease enter a output file: ")    
                    
                #Instantiate a CaesarCipher class with the inputted cipher key 
                cipher = CaesarCipher(cipherkey)
                
                if input_type == 'message':
                    #Calling the decrypt method 
                    print(cipher.decrypt(ciphertext))
                else:
                    
                    cipher.decrypt_file(ciphertext,output_file)
                
    def analyze_letter_frequency(self):
        #Instantiate the LetterFrequencyDistribution class and prompt user for file 
    
            letter_dist = LetterFrequencyDistribution(input("Please enter the file you want to analyze: "))
            
            # Calling the analyze_file method to return frequencies analysis
            letter_dist.analyze_file()         
