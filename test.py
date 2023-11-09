import string
import math
# abstract base class work
from abc import ABC, abstractmethod
alphabet = list(string.ascii_uppercase)
n_alphabet = []
for s in alphabet:
    n_alphabet.append(" " + s)


sentence = "This is a sample sentence."
# Create a dictionary to store the counts of each alphabet
letter_count = {letter: 0 for letter in string.ascii_uppercase}

# Convert the sentence to uppercase to ensure case-insensitivity
sentence = sentence.upper()

# Iterate through the characters in the sentence
for char in sentence:
    if char.isalpha():  # Check if the character is an alphabet letter
        letter_count[char] += 1
        
length = sum(letter_count.values())
for letter in letter_count:
    letter_count[letter] = (letter_count[letter] / length) * 100

# Print the counts
total_width = 87
spaces_before_line = 4

for letter, percentage in letter_count.items():
    #formatted_percentage = float(formatted_percentage)
    if percentage>10:  
        line = "|{}-{:.2f}%".format(letter, percentage)
    else:
        line = "|{}- {:.2f}%".format(letter, percentage)
    output_line = " " * spaces_before_line + line.rjust(total_width - spaces_before_line)
    print(output_line)

print(f'_'*78)
for item in n_alphabet:
    print(item, end=' ')


""" print('{:<78s}{}'.format("", "|A-TEST"))
 """