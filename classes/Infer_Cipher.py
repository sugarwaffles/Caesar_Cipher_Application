#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
from classes.Letter_Dist import LetterFrequencyDistribution
import os
class breakCaesarCipher(LetterFrequencyDistribution):
    def __init__(self, input_file):
        super().__init__(input_file)
        self.reference_file = None
        self.sorted_reference_freq = None
        self.sorted_input_freq = self.get_sorted_frequencies()
        
    # Inherit sorted frequencies method for letter freq of input file    
    def get_sorted_frequencies(self):
        return super().sort_frequencies().get_sorted_list() # Call the method and then get the sorted list
    
    # Sets the reference file name and the frequency of letters sorted
    def reference_file_analysis(self, reference_file):
        self.reference_file = reference_file
        self.sorted_reference_freq = self.sort_reference_file()
        
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
        if self.sorted_input_freq:
            return self.sorted_input_freq[0][0]
        else:
            return None

    def get_top_frequency_letter_reference(self):
        if self.sorted_reference_freq:
            return self.sorted_reference_freq[0][0]
        else:
            return None
        
    def calculate_cipher_key(self):
        # Retrieve the top freq letter from both input and reference file, standardize by setting to lower case
        input_letter = self.get_top_frequency_letter_input().lower()
        reference_letter = self.get_top_frequency_letter_reference().lower()

        if input_letter and reference_letter:
            # Calculate the difference in positions
            input_position = ord(input_letter) - ord('A')
            reference_position = ord(reference_letter) - ord('A')

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
