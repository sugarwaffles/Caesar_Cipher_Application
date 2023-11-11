import string

class SortedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.nextNode = None

    def __init__(self):
        self.headNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        self.length += 1
        # If list is currently empty
        if self.headNode is None:
            self.headNode = newNode
            return
        # Check if it is going to be new head
        if newNode.data < self.headNode.data:
            self.__appendToHead(newNode)
            return
        # Check if it is going to be inserted between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode is not None:
            if newNode.data < rightNode.data:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # Once we reach here it must be added at the tail
        leftNode.nextNode = newNode

class LetterFrequencyDistribution:
    def __init__(self, filename):
        self.filename = filename

    def analyze_file(self):
        with open(self.filename, 'r') as file:
            text = file.read().lower()
            letter_counts = {letter: text.count(letter) for letter in string.ascii_lowercase}
            total_letters = sum(letter_counts.values())

            # Calculate frequencies
            frequencies = {k: round(v / total_letters * 100, 2) for k, v in letter_counts.items()}

            # Print top 5 frequencies
            top5_freq_table = []
            # Setting the "Headers" for TOP 5 FREQ
            top5_freq_table.append("TOP 5 FREQ")
            top5_freq_table.append("-" * 11)

            # Top 5 letter freq sorted by frequency and alphabetically if same freq
            sorted_top5 = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

            # Take only the top 5
            sorted_top5 = sorted_top5[:5]

            # Print top 5 frequencies
            for letter, frequency in sorted_top5:
                if frequency > 10:
                    top5_freq_table.append(f"| {letter.upper()} -{frequency}%")
                else:
                    top5_freq_table.append(f"| {letter.upper()} - {frequency}%")

            # Total width represents the num of characters(space in this case) to fill the missing spaces (to the left of the str) which will be used for the y-axis creation
            total_width = 80

            # Create a list to store the histogram
            histogram = []

            # Populate the histogram with '*' for each letter
            for y_index in range(25, -1, -1):  # Start from Z and go backward
                line = ''
                for letter in string.ascii_uppercase:  # Use ascii_uppercase for X-axis labels
                    count = letter_counts.get(letter.lower(), 0)
                    # Only print a ' * ' when
                    if count > y_index:
                        line += ' * '
                    else:
                        line += '   '

                histogram.append(line)
            
            line_counter = 0

            for line_hist, letter in zip(histogram, string.ascii_uppercase):
                percentage = frequencies.get(letter.lower(), 0)

                # Find starting level for TOP 5 FREQ table
                if 'K' <= letter <= 'Q':
                    # Only print if there are lines left in top5_freq_table
                    if line_counter < len(top5_freq_table):
                        line = "{} | {}- {:.2f}% {:>15s}".format(line_hist, letter, percentage, top5_freq_table[line_counter])
                        line = " " + line.rjust(total_width)
                        print(line)
                        line_counter += 1
                else:
                    # Formatting double-digit percentages
                    if percentage > 10:
                        line = "{} | {}-{:.2f}%".format(line_hist, letter, percentage)
                    else:
                        line = "{} | {}- {:.2f}%".format(line_hist, letter, percentage)

                    # Reset spaces before line after finishing printing TOP 5 FREQ table to the right of the y-axis

                    output_line = " " + line.rjust(total_width)
                    print(output_line)

            # Print "X axis" using the correct unicode U+2500 (box drawing single horizontal line)
            print('\u2500' * (total_width))

            # Print bottom letters
            print(' ', end=' ')
            for letter in string.ascii_uppercase:
                print(f"{letter}  ", end='')
            print()

















