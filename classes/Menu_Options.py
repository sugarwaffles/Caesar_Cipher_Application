# Name: Wilfred Djumin
# Class: DAAA/FT/2B05
import string
import os
from classes.Encrypt_Decrypt import CaesarCipher, CaesarCipherMessage, CaesarCipherFiles
from classes.Letter_Dist import LetterFrequencyDistribution
from classes.Infer_Cipher import BreakCaesarCipher
from classes.Analyze_Sort_Files import AnalyzeSortFiles
from classes.Cipher_Handler import CipherHandler
from classes.Input_Handler import InputHandler
from classes.Dictionary_Attack import DictionaryAttack, PureBruteForceAttack


class MenuOptions:
    def __init__(self):
        self.cipher_handler = CipherHandler()
        self.input_handler = InputHandler()
        # dictionary storing options from 1 - 8
        self.__menu_options = {
            1: 'Encrypt/Decrypt Message',
            2: 'Encrypt/Decrypt File',
            3: 'Analyze letter frequency distribution',
            4: 'Infer Caesar cipher key from file',
            5: 'Analyze and sort encrypted files',
            6: 'Brute Decrypt Caesar Cipher with English Dictionary / Words',
            7: 'Extra Option Two',
            8: 'Exit'
        }

    def get_menu_options(self):
        return self.__menu_options

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
        self.press_enter()

    def print_menu(self):
        print("\nPlease select your choice: (1,2,3,4,5,6,7,8)")
        # Looping through dictionary to list options to user
        for choice, description in self.get_menu_options().items():
            print(f"\t {choice}. {description}")

    def get_choice(self):
        while True:
            try:
                # Prompt user for choice
                choice = int(input("Enter your choice: "))

                # Check if the choice exists in the menu_options dictionary
                if choice in self.get_menu_options():
                    # Ask user for confirmation
                    confirm_choice = input(
                        f'You chose option {choice}: {self.get_menu_options().get(choice)}. Confirm? (y/n): ').lower()

                    # Use confirmation_validator and check if the result is not None
                    confirmed_choice = self.confirmation_validator(
                        confirm_choice, choice)
                    if confirmed_choice is not None:
                        return confirmed_choice

                # If not, prompt user to re-enter a number between 1 and 8
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.\n")

            # Raise ValueError if the user does not input a number/integer
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
            self.infer_caesar_key_and_decrypt()
        elif choice == 5:
            self.analyze_encrypted_files()
        elif choice == 6:
            self.dictionary_attack()
            # Brute force way of decrypting caesar cipher
        elif choice == 7:
            self.visualize_caesar_cipher()
            #
        elif choice == 8:
            # Execute a clean exit if user presses 8
            print(
                "Bye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer")
            exit(0)

    def get_non_empty_input(self, prompt):
        return self.input_handler.get_non_empty_input(prompt)

    def get_file_path(self, file_name):
        return self.input_handler.get_file_path(file_name)

    def get_folder_path(self, file_name):
        return self.input_handler.get_folder_path(file_name)

    def input_file(self):
        return self.input_handler.input_file()

    def press_enter(self):
        return self.input_handler.press_enter()

    def confirmation_validator(self, input, choice):
        return self.input_handler.confirmation_validator(input, choice)

    def get_valid_cipherkey(self):
        return self.cipher_handler.get_valid_cipherkey()

    def get_action_input(self):
        return self.cipher_handler.get_action_input()
    
    def handle_encryption_decryption(self, input_type):
        while True:
            # Prompts user for E or D , returns back
            action = self.get_action_input()

            # Prompt Depending on input type which is based on the choice selected and action being returned
            user_input_prompt = f"\nPlease type {input_type} you want to {'encrypt' if action == 'encrypt' else 'decrypt'}: "
            user_input = self.get_non_empty_input(user_input_prompt)

            #Check if input file exists
            if input_type == 'file':
                input_path = self.get_file_path(user_input)
                if input_path is None:
                    break
                
                cipherkey = self.get_valid_cipherkey()
                output_file = self.get_non_empty_input("\nPlease enter an output file: ")
                # Pass the correct transformation direction to process_file
                self.cipher_handler.process_file(cipherkey, input_path, output_file, action)
            else:
                cipherkey = self.get_valid_cipherkey()
                cipher = self.cipher_handler.get_cipher_instance(cipherkey, input_type)
                # Pass the correct transformation direction to transform_message
                result = cipher.transform_message(user_input, action)
                print(result)

            break
    # This whole function handles choice 3

    def analyze_letter_frequency(self):
        while True:
            letter_dist_input = self.input_file()
            file_path = self.get_file_path(letter_dist_input)
            if file_path is None:
                break
            else:
                letter_dist = LetterFrequencyDistribution(file_path)
                letter_dist.analyze_file()
                self.press_enter()

            break
    # This whole function handles choice 4

    def infer_caesar_key_and_decrypt(self):
        while True:
            input_file_analyze = self.input_file()
            input_file_path = self.get_file_path(input_file_analyze)
            if input_file_path is None:
                break

            cipher_breaker = BreakCaesarCipher(input_file_path)

            input_reference_file = self.get_non_empty_input(
                "\nPlease enter the reference frequencies file: ")
            file_path_ref = self.get_file_path(input_reference_file)

            if file_path_ref is None:
                break

            # Check if the reference file has a valid format
            sorted_reference_freq = cipher_breaker.reference_file_analysis(
                file_path_ref)
            if sorted_reference_freq is None:
                break

            cipher_key = cipher_breaker.calculate_cipher_key()
            
            if cipher_key == 0:
                print("File contents are already in Plaintext, Exiting...")
                break
                
            
            print(f"The inferred caesar cipher key is: {cipher_key}")

            prompt_for_decryption = self.get_non_empty_input(
                "\nWould you want to decrypt this file using the key? y/n: ")

            if self.confirmation_validator(prompt_for_decryption, choice=None):
                cipherkey = cipher_key
                output_file = self.get_non_empty_input(
                    "\nPlease enter an output file: ")
                self.cipher_handler.decrypt_file(
                    cipherkey, input_file_path, output_file)
                self.press_enter()
                break
            else:
                print(
                    f"Selected '{prompt_for_decryption}', back to menu options...")
                break

    # This whole function handles choice 5
    def analyze_encrypted_files(self):

        while True:
            folder_name = self.get_non_empty_input(
                "\nPlease enter the folder name for batch decryption: ")

            folder_path = self.get_folder_path(folder_name)
            if folder_path is None:
                break

            analyzer = AnalyzeSortFiles(folder_path)
            perform_analysis = analyzer.analyze_and_sort_files()
            if perform_analysis is None:
                break
            print("\nBatch decryption completed successfully.")
            self.press_enter()
            break
    # Option 6

    def dictionary_attack(self):
        while True:
            # Handle input file
            input_file = self.input_file()
            input_file_path = self.get_file_path(input_file)
            if input_file_path is None:
                break

            # Initialize file_path_ref
            file_path_ref = None

            # Handle reference file
            prompt_use_dictionary = self.get_non_empty_input(
                "\nWould you like to use a reference (List of English words) for the decryption? Y / N: ")
            confirm_prompt = self.confirmation_validator(
                prompt_use_dictionary, choice=None)
            if confirm_prompt is None:
                break
            # User wants to use a reference file
            elif confirm_prompt:
                # Ask for default or user-specified reference file
                use_default_dict = self.get_non_empty_input(
                    "\nWould you like to use the default English words dictionary (479k words)? Y / N: ")
                use_default_dict = self.confirmation_validator(
                    use_default_dict, choice=None)
                if use_default_dict is None:
                    break

                # Set file_path_ref based on the user's choice
                if use_default_dict:
                    file_path_ref = self.get_file_path("all-words.txt")
                else:
                    reference_file_selection = self.get_non_empty_input(
                        "\nPlease enter the reference dict file: ")
                    file_path_ref = self.get_file_path(
                        reference_file_selection)

                    if file_path_ref is None:
                        break

            # User wants to perform a pure brute force attack
            else:
                print(f"\nUsing pure brute force decryption...")
                file_path_ref = None

            # Get the output file from the user
            output_file = self.get_non_empty_input(
                "\nPlease enter an output file: ")

            if file_path_ref:
                # Create an instance of the DictionaryAttack class
                dict_attack = DictionaryAttack(input_file_path, file_path_ref)
                # Perform the dictionary attack
                decrypted_text, key = dict_attack.dictionary_attack_file(
                    input_file_path, use_dictionary=True, output_file=output_file)
            else:
                # Create an instance of the PureBruteForceAttack class
                brute_force_attack = PureBruteForceAttack(input_file_path)
                # Perform the pure brute force attack
                (best_result, all_results) = brute_force_attack.perform_attack()
                # print(all_results)

                # Get the ciphertext from the PureBruteForceAttack instance
                ciphertext = brute_force_attack.read_ciphertext()

                # Write the results to the output file
                brute_force_attack.write_results_to_file(
                    output_file, best_result, all_results)

                # Unpack the best result
                decrypted_text, key, _ = best_result

            # If user uses
            if decrypted_text is not None and file_path_ref is not None:
                print(f"\nDecrypted Text:\n{decrypted_text}")
                print(f"\nCipher Key: {key}")
                print(f"\nOutput File Name: {output_file}")
                # Add the final results to an output file
                break
            else:
                # If user uses own reference dict/words file
                if file_path_ref is not None:
                    print(
                        "Decryption unsuccessful, please try using the full English dictionary for better accuracy!")
                    break
                # If user uses pure brute force
                else:
                    print(
                        f"Check the output file: '{output_file}' for a recognizable english sentence! ")
                    break
