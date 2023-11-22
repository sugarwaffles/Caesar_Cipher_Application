import os
import string
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
            print(f"Error: File '{file_name}' not found.")
            return None

    @staticmethod
    def create_output_file(output_filename):
        # Ensure the "Dataset" directory exists
        dataset_dir = os.path.join(os.path.dirname(__file__), "..", "Dataset")
        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir)

        # Check if the output filename has a .txt extension
        if not output_filename.lower().endswith(".txt"):
            print("Error: Output filename must end with '.txt'")
            return None  # Return None if the filename doesn't end with .txt

        # Normalize the output filename to handle invalid characters
        normalized_output_filename = os.path.normpath(output_filename)

        # Remove invalid characters from the file name
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        sanitized_output_filename = ''.join(c for c in normalized_output_filename if c in valid_chars)

        # Split the sanitized output_filename into directory and file name components
        output_dir, output_file = os.path.split(sanitized_output_filename)

        # Create the full path for the output file in the "Dataset" directory
        return os.path.join(dataset_dir, output_file)

    def confirmation_validator(self, user_input, choice=None):
        if choice is not None:
                # Handling confirmation for menu choices
                if user_input.lower() == 'y':
                    return choice
                elif user_input.lower() == 'n':
                    print('Operation canceled. Please choose again.\n')
                    return None
                else:
                    print('Error: Invalid confirmation. Please enter "y" for yes or "n" for no.\n')
                    return None
        else:
            # Handling confirmation for other scenarios
            if user_input.lower() == 'y':
                return True
            elif user_input.lower() == 'n':
                return False
            else:
                print('Error: Invalid input. Please enter "y" for yes or "n" for no.\n')
                return None

    @staticmethod
    def press_enter():
        return input("\nPress enter key to continue...")

    @staticmethod
    def input_file():
        return input("Please enter the file you want to analyze: ")