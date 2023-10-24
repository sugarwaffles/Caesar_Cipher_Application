
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
        print('*********************************************************************** \n\n')
        
    def print_menu(self):
        print("Please select your choice: (1,2,3,4,5,6,7,8)")
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
                



    # existing code here
