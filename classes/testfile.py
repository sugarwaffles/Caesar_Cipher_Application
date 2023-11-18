import os

current_directory = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_directory, "..", "Dataset")
file_path = os.path.join(dataset_path, "TwinkleStar.txt")

try:
    # Ensure the Dataset directory exists
    os.makedirs(dataset_path, exist_ok=True)

    # Check if the file exists and print its contents
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            print(f"File '{file_path}' exists. Contents:")
            print(file.read())
    else:
        print(f"File '{file_path}' does not exist. Creating...")

    # Open the file for writing and create it if it doesn't exist
    with open(file_path, "w") as file:
        print(f"File '{file_path}' opened successfully.")
        file.write('asdasd')

    print(f"File '{file_path}' created/updated successfully.")
except Exception as e:
    print(f"Error creating or updating the file: {e}")
