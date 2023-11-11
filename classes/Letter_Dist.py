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
    current_node = sorted_list.head
    top5_nodes = sorted([(node.letter, node.frequency) for node in iter_nodes(current_node)], key=lambda x: (-x[1], x[0]))[:5]
    for letter, frequency in top5_nodes:
        print(f"{letter} - {frequency}%")

def iter_nodes(node):
    while node:
        yield node
        node = node.next

class LetterFrequencyDistribution:
    def __init__(self, filename):
        self.filename = filename

    import collections
import string

class LetterFrequencyDistribution:
    def __init__(self, filename):
        self.filename = filename

    def analyze_file(self):
        with open(self.filename, 'r') as file:
            text = file.read().lower()
            letter_counts = collections.Counter(c for c in text if c.isalpha())
            total_letters = sum(letter_counts.values())

            # Calculate frequencies
            frequencies = {k: round(v / total_letters * 100, 2) for k, v in letter_counts.items()}

            # Find maximum frequency
            max_frequency = max(frequencies.values())

            # Print top 5 frequencies
            top5_freq_table = []
            # Setting the "Headers" for TOP 5 FREQ
            top5_freq_table.append("TOP 5 FREQ")
            top5_freq_table.append("-" * 11)

            # Top 5 letter freq sorted by alphabets if same freq
            for letter, frequency in sorted(frequencies.items(), key=lambda x: (-x[1], x[0].upper()))[:5]:
                if frequency > 10:
                    top5_freq_table.append(f"| {letter.upper()} -{frequency}%")
                else:
                    top5_freq_table.append(f"| {letter.upper()} - {frequency}%")
            spaces_before_line = 10
            total_width = 80
            line_counter = 0

            # Create a list to store the histogram
            histogram = []

            # Populate the histogram with '*' for each letter
            for y_index in range(25, -1, -1):  # Start from Z and go backward
                line = ''
                for x_index, letter in enumerate(string.ascii_uppercase):  # Use ascii_uppercase for X-axis labels
                    percentage = frequencies.get(letter.lower(), 0)

                    if percentage >= y_index:
                        line += ' * '
                    else:
                        line += '   '
                
                histogram.append(line)

            # Print TOP 5 FREQ table
            line_counter = 0
            for i, (line_hist, letter) in enumerate(zip(histogram, string.ascii_uppercase)):
                percentage = frequencies.get(letter.lower(), 0)

                # Find starting level for TOP 5 FREQ table
                if 'K' <= letter <= 'Q':
                    # Only print if there are lines left in top5_freq_table
                    if line_counter < len(top5_freq_table):
                        line = "| {}- {:.2f}% {:>15s}".format(letter, percentage, top5_freq_table[line_counter])
                        spaces_before_line = 26
                        line = " " * spaces_before_line + line.rjust(total_width)
                        print(line)
                        line_counter += 1
                else:
                    if percentage > 10:
                        line = "{} | {}-{:.2f}%".format(line_hist, letter, percentage)
                    else:
                        line = "{} | {}- {:.2f}%".format(line_hist, letter, percentage)

                    # Reset spaces before line after finishing printing TOP 5 FREQ table to the right of the y-axis
                    spaces_before_line = 10
                    output_line = " " + line.rjust(total_width)
                    print(output_line)

            # Print "X axis" using the correct unicode U+2500 (box drawing single horizontal line)
            print('\u2500' * (total_width))  # Added +3 for better alignment

            # Print bottom letters
            print(' ', end=' ')
            for letter in string.ascii_uppercase:
                print(f"{letter}  ", end='')
            print()
            















