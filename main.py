from classes.Menu_Options import MenuOptions
from classes.Encrypt_Decrypt import CaesarCipher
from classes.Letter_Dist import LetterFrequencyDistribution

if __name__ == "__main__":
    
    #Instantiate the MenuOptions class
    menu = MenuOptions()
    
    # Display essential information calling the start() method in MenuOptions class
    menu.start()
    
    # Prompt user to press "Enter" key 
    starting_input = input("Press Enter to continue...")
    
    while True:
    
    
        if len(starting_input) != 0:
            print("You typed some text before pressing enter! Please retry.")
            break
            
        menu.print_menu()
        choice = menu.get_choice()

        if choice == 1:
            
            action = ''
            
            # Continuously prompt the user until valid input is provided "E" or "D" (case sensitive) 
            while action != "E" and action != 'D':
                action = input('\nEnter "E" for Encrypt or "D" for Decrypt: ')
                
                # Display error message if the input is not E or D
                if action != "E" and action != 'D':
                    print("Only enter either 'E' or 'D' (case sensitive)")
            
            # Encrypt or decrypt based on the user's action/input
            if action == "E":
                
                plaintext = input("\nPlease type text you want to encrypt: ")
                cipherkey = int(input("\nEnter the cipher key: \n"))
                
                #Instantiate a CaesarCipher class with the inputted cipher key 
                cipher = CaesarCipher(cipherkey)
                
                #Calling the encrypt method 
                print(cipher.encrypt(plaintext))
                
            elif action == 'D':
                ciphertext = input("\nPlease type text your want to decrypt: ")
                cipherkey = int(input("\nEnter the cipher key: "))
                
                #Instantiate a CaesarCipher class with the inputted cipher key 
                cipher = CaesarCipher(cipherkey)
                
                #Calling the decrypt method 
                print(cipher.decrypt(ciphertext))
                
        elif choice == 2:
            menu.encrypt_decrypt_file()
            
        elif choice == 3:
            #Instantiate the LetterFrequencyDistribution class and prompt user for file 
    
            letter_dist = LetterFrequencyDistribution(input("Please enter the file you want to analyze: "))
            
            # Calling the analyze_file method to return frequencies analysis
            letter_dist.analyze_file()    
        
        elif choice == 4:
            pass
            
        elif choice == 5:
            pass
        
        elif choice == 6:
            pass
            
        elif choice == 7:
            pass

        elif choice == 8:
            print("Bye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer")
            break
