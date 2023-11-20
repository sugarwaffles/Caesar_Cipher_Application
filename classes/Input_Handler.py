import os

class InputHandler:
    @staticmethod
    def get_non_empty_input(prompt):
        user_input = input(prompt)
        while not user_input.strip():
            print("Input cannot be empty. Please try again.")
            user_input = input(prompt)
        return user_input

    @staticmethod
    def get_file_path(file_name):
        file_path = os.path.join(os.path.dirname(__file__), "..", "Dataset")
        files_in_directory = [f for f in os.listdir(file_path)]
        if file_name in files_in_directory:
            return os.path.join(file_path, file_name)
        else:
            print(f"File {file_name} not found.")
            return None

    @staticmethod
    def press_enter():
        return input("\nPress enter key to continue...")
    
    @staticmethod
    def input_file():
        return input("Please enter the file you want to analyze: ")