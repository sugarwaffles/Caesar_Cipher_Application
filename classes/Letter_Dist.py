import collections
import string


class Node:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, letter, frequency):
        new_node = Node(letter, frequency)

        if not self.head or frequency > self.head.frequency:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and frequency <= current.next.frequency:
                current = current.next
            new_node.next = current.next
            current.next = new_node

def print_top5_frequencies(sorted_list):
    current = sorted_list.head
    top5 = sorted([(node.letter, node.frequency) for node in iter_nodes(current)], key=lambda x: (-x[1], x[0]))[:5]
    for letter, frequency in top5:
        print(f"{letter} - {frequency}%")

def iter_nodes(node):
    while node:
        yield node
        node = node.next
import string
import collections


class LetterFrequencyDistribution:
    def __init__(self, filename):
        self.filename = f"./Dataset/{filename}"

    def analyze_file(self):
        with open(self.filename, 'r') as file:
            text = file.read().lower()
            letter_counts = collections.Counter(c for c in text if c.isalpha())
            total_letters = sum(letter_counts.values())

            # Calculate frequencies
            frequencies = {k: round(v / total_letters * 100, 2) for k, v in letter_counts.items()}
            print(frequencies)

            # Find maximum frequency
            max_frequency = max(frequencies.values())

            # Print top 5 frequencies
            print("Top 5 frequencies:")
            for letter, frequency in sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"{letter} - {frequency}%")

            # Print the frequency distribution chart

            

            # Add empty line before printing the histogram
            print()

            # Print histogram for all alphabets
            for i in range(int(max(frequencies.values())) + 1, 0, -1):
                line = ''
                for letter in string.ascii_uppercase:  # Use ascii_uppercase for Y-axis labels
                    percentage = frequencies.get(letter.lower(), 0)
                    if percentage >= i:
                        line += ' * '
                    else:
                        line += '   '
                print(line)
            # Y-axis line
            spaces_before_line = 10  # Adjust this value as needed
            total_width = 78  # Adjust this value as needed
            for i, letter in enumerate(string.ascii_uppercase):
                percentage = frequencies.get(letter.lower(), 0)
                if percentage > 10:
                    line = "| {}-{:.2f}%".format(letter, percentage)
                else:
                    line = "| {}- {:.2f}%".format(letter, percentage)
                output_line = " " * spaces_before_line + line.rjust(total_width)
                print(output_line)
                
            # Print "X axis"
            print('_' * 78)

            # Print bottom letters
            print(' ', end='')
            for letter in string.ascii_uppercase:
                print(f"{letter}  ", end='')
            print()


# Example usage
filename = "TwinkleStar.txt"  # Replace with your actual file name
analyzer = LetterFrequencyDistribution(filename)
analyzer.analyze_file()














