from classes.Menu_Options import MenuOptions
# from classes.encryption import Encryption
# from classes.decryption import Decryption
# from classes.file_handler import FileHandler
# from classes.sorted_list import SortedList

if __name__ == "__main__":
    
    #Instantiate the MenuOptions class
    menu = MenuOptions()
    
    # Display essential information calling the start() method in MenuOptions class
    menu.start()
    
    # Prompt user to press "Enter" key 2
    
    input("Press Enter to continue...")
    
    
    while True:
        
        menu.print_menu()
        choice = menu.get_choice()

        if choice == 1:
            menu.encrypt_decrypt_message()
            
        elif choice == 2:
            menu.encrypt_decrypt_file()
            
        elif choice == 3:
            pass
        
        elif choice == 4:
            pass
            
        elif choice == 5:
            pass
        
        elif choice == 6:
            pass
            
        elif choice == 7:
            pass

        elif choice == 8:
            print("Exiting the application. Goodbye!")
            break
