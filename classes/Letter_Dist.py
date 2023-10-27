#Working function but have not integrated to match the main.py class yet

import collections
import string

class LetterFrequencyDistribution:
    
    def __init__(self, filename): 
        
        # Define the folder directory for where the .txt files are stored at
        self.filename = f"./Dataset/{filename}"

    def analyze_file(self):
        with open(self.filename, 'r') as file:
            text = file.read().lower()
            letter_counts = collections.Counter(c for c in text if c.isalpha())
            total_letters = sum(letter_counts.values())
            
            # Calculate frequencies
            frequencies = {k: round(v / total_letters * 100, 2) for k, v in letter_counts.items()}
            
            # Print histogram for all alphabets
            for i in range(int(max(frequencies.values())) + 1, 0, -1):
                print(' '.join('*' if frequencies.get(letter, 0) >= i else ' ' for letter in string.ascii_lowercase))
            
            # Print letters
            print(' '.join(string.ascii_lowercase))
            
            # Print top 5 frequencies
            print("\nTop 5 frequencies:")
            sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
            for letter, freq in sorted_frequencies[:5]:
                print(f"{letter} - {freq}%")











