#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
from classes.Letter_Dist import LetterFrequencyDistribution
import os
class BreakCaesarCipher(LetterFrequencyDistribution):
    def __init__(self, input_file):
        super().__init__(input_file)
        self.reference_file = None
        self.sorted_reference_freq = None
        self.sorted_input_freq = self.get_sorted_frequencies()
        
    # Inherit sorted frequencies method for letter freq of input file    
    def get_sorted_frequencies(self):
        return super().sort_frequencies() # Call the method and then get the sorted list
    
    def is_valid_reference_file(self, reference_file):
        try:
            with open(reference_file, 'r') as file:
                lines = file.readlines()

            # Check if each line can be split into two parts by a comma
            for line in lines:
                parts = line.split(',')
                if len(parts) != 2:
                    return False

                # Check if the second part is a valid float
                float(parts[1])

            return True
        except Exception as e:
            return False

    def reference_file_analysis(self, reference_file):
        if not self.is_valid_reference_file(reference_file):
            print("Invalid reference file format. Each line should contain a letter and a frequency separated by a comma.")
            return None

        self.reference_file = reference_file
        self.sorted_reference_freq = self.sort_reference_file()
        return self.sorted_reference_freq  # Return the sorted frequencies
    # Sorts the letters by frequency in the reference file
    def sort_reference_file(self):
        with open(self.reference_file, 'r') as file:
            lines = file.readlines()

        # Extract letters and frequencies from each line
        reference_freq = [(line.split(',')[0], float(line.split(',')[1])) for line in lines]

        # Sort by frequency in descending order
        sorted_reference_freq = sorted(reference_freq, key=lambda x: x[1], reverse=True)

        return sorted_reference_freq
    
    def get_top_frequency_letter_input(self):
        # Making use of SortedList method we added to get letter at first index, which would be the letter of max frequency
        #print(self.sorted_input_freq.get_letter_at_index(0))
        return self.sorted_input_freq.get_letter_at_index(0)

    def get_top_frequency_letter_reference(self):
        # Retreive the top letter along with frequency, then return only the letter
        top_item = self.sorted_reference_freq[0]
        return top_item[0] if top_item else None

        
    def calculate_cipher_key(self):
        # Retrieve the top freq letter from both input and reference file, standardize by setting to lower case
        input_letter = self.get_top_frequency_letter_input()
        reference_letter = self.get_top_frequency_letter_reference()

        if input_letter is not None and reference_letter is not None:
            # Standardize to lowercase
            input_letter = input_letter.lower()
            reference_letter = reference_letter.lower()

            # Calculate the difference in positions
            input_position = ord(input_letter) - ord('a')
            reference_position = ord(reference_letter) - ord('a')

            # Calculate the cipher key
            cipher_key = (input_position - reference_position) % 26

            return cipher_key
        else:
            return None
        

# # Example usage
# cipher_breaker = breakCaesarCipher(os.path.join(os.path.dirname(__file__), "..", "Dataset",'test2.txt'))
# cipher_breaker.reference_file_analysis(os.path.join(os.path.dirname(__file__), "..", "Dataset",'englishtext.txt'))

# # Access the sorted reference frequencies
# sorted_reference = cipher_breaker.sorted_reference_freq
# sorted_freq_input = cipher_breaker.sort_frequencies()
# print(cipher_breaker.get_top_frequency_letter_input(),cipher_breaker.get_top_frequency_letter_reference())
