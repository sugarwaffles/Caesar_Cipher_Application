#Name: Wilfred Djumin
#Class: DAAA/FT/2B05


from classes.Menu_Options import MenuOptions
# from classes.Encrypt_Decrypt import CaesarCipher
# from classes.Letter_Dist import LetterFrequencyDistribution

if __name__ == "__main__":
    
    #Instantiate the MenuOptions class
    menu = MenuOptions()
    
    # Display essential information calling the start() method in MenuOptions class
    menu.start()

    while True:
        menu.print_menu()
        choice = menu.get_choice()
        menu.handle_choice(choice)
