from classes.Menu_Options import MenuOptions
# from classes.Encrypt_Decrypt import CaesarCipher
# from classes.Letter_Dist import LetterFrequencyDistribution

if __name__ == "__main__":
    
    #Instantiate the MenuOptions class
    menu = MenuOptions()
    
    # Display essential information calling the start() method in MenuOptions class
    menu.start()
    
    # Prompt user to press "Enter" key 
    # starting_input = input("Press Enter to continue...")
    
    while True:
        # if len(starting_input) != 0:
        #     print("You typed some text before pressing enter! Please retry.")
        #     break
        menu.print_menu()
        choice = menu.get_choice()
        menu.handle_choice(choice)
