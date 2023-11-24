#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
import string ,os

# Parent Class Node
class Node:
    def __init__(self, data):
        # Initialize a Node with data and a pointer to the next Node
        self.data = data
        self.nextNode = None

    def get_data(self):
        # Get the data of the Node
        return self.data

    def get_next(self):
        # Get the next Node
        return self.next

    def set_data(self, new_data):
        # Set the data of the Node
        self.data = new_data

    def set_next(self, new_next):
        # Set the next Node
        self.next = new_next

    def get_letter(self):
        # Get the first character of the data (assuming data is a tuple)
        return self.data[0]

    def get_frequency(self):
        # Get the second element of the data (assuming data is a tuple)
        return self.data[1]

# Child Class LetterNode


class LetterNode(Node):
    def __lt__(self, other):
        # Compare frequencies and, if equal, compare letters
        return self.data[1] > other.data[1] or (self.data[1] == other.data[1] and self.data[0] < other.data[0])

    def get_data(self):
        # Get the data of the LetterNode
        return self.data

# SortedList class


class SortedList:
    def __init__(self):
        # Initialize a SortedList with a headNode and a length counter
        self.headNode = None
        self.length = 0

    def append_to_head(self, newNode):
        # Insert a Node at the beginning of the SortedList
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        # Insert a Node in a sorted manner into the SortedList
        self.length += 1

        if self.headNode is None:
            # If the list is empty, make the new Node the head
            self.headNode = newNode
            return

        if newNode < self.headNode:
            # If the new Node should be the new head, insert it at the beginning
            self.append_to_head(newNode)
            return

        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode is not None:
            # Iterate through the list to find the correct position for the new Node
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        leftNode.nextNode = newNode

    def __str__(self):
        # Return a string representation of the SortedList
        output = ""
        node = self.headNode
        firstNode = True
        while node is not None:
            if firstNode:
                output = node.get_data().__repr__()
                firstNode = False
            else:
                output += (',' + node.get_data().__repr__())
            node = node.nextNode
        return output

    def get_data_at_index(self, index):
        # Get the data of the Node at a specific index in the SortedList
        current_node = self.headNode
        current_index = 0

        while current_node is not None and current_index < index:
            current_node = current_node.nextNode
            current_index += 1

        if current_index == index and current_node is not None:
            return current_node.get_data()

        return None

    def get_letter_at_index(self, index):
        # Get the letter at a specific index in the SortedList
        data = self.get_data_at_index(index)
        return data[0] if data else None

    def get_sorted_list(self):
        # Get the data of the SortedList as a dictionary of letters and frequencies
        sorted_dict = {}
        node = self.headNode
        while node is not None:
            letter, freq = node.get_data()
            sorted_dict[letter] = freq
            node = node.nextNode
        return sorted_dict


class LetterFrequencyDistribution:
    def __init__(self, filename):
        # Initialize a LetterFrequencyDistribution with a filename, letter_counts, frequencies, and sorted_frequencies
        self.__filename = filename
        self.letter_counts, self.frequencies = self.calculate_letter_counts_and_frequencies()
        self.sorted_frequencies = self.sort_frequencies()

    def get_filename(self):
        # Get the filename
        return self.__filename

    def calculate_letter_counts_and_frequencies(self):
        # Calculate letter counts and frequencies from the contents of the file
        with open(self.get_filename(), 'r') as file:
            text = file.read().lower()
            letter_counts = {letter: text.count(
                letter) for letter in string.ascii_lowercase}
            total_letters = sum(letter_counts.values())
            frequencies = {k: round(v / total_letters * 100, 2)
                           for k, v in letter_counts.items()}
        return letter_counts, frequencies

    def analyze_file(self):

        # Print top 5 frequencies
        top5_freq_table, _ = self.calculate_top5_frequencies(
            include_headers=True)

        # Total width represents the num of characters(space in this case) to fill the missing spaces (to the left of the str) which will be used for the y-axis creation
        total_width = 80

        # Create a list to store the histogram
        histogram = self.create_histogram()

        # Print the histogram
        self.print_histogram_with_Yaxis(
            histogram, total_width, top5_freq_table)

        # Print the X-axis
        self.X_axis(total_width)

    def sort_frequencies(self):
        # Create a SortedList instance
        sorted_freq = SortedList()

        # Iterate over the dictionary items ('self.frequencies' is a dictionary like {'a': 3, 'b': 5, 'c': 2, ...})
        for letter, frequency in self.frequencies.items():
            # Create a LetterNode instance with [letter, frequency]
            letter_node = LetterNode([letter, frequency])

            # Insert the LetterNode into the sorted list based on freq then alphabet since we override the __lt__ operator
            sorted_freq.insert(letter_node)

        # Return the sorted linked list
        return sorted_freq

    def calculate_top5_frequencies(self, include_headers=True):
        top5_freq_list = []
        top5_freq_dict = {}

        #
        if include_headers:
            # Appending the headers of the TOP 5 FREQ table
            top5_freq_list.append("TOP 5 FREQ")
            top5_freq_list.append("-" * 11)

        current_node = self.sorted_frequencies.headNode
        
        # Iterate over the first five nodes in the sorted list

        for current_node in range(5):
            if current_node is None:
                break
            letter, frequency = self.sorted_frequencies.get_data_at_index(current_node)

            # Skip headers if not required
            if not include_headers:
                continue
            # For double digit frequencies, format it differently
            if frequency > 10:
                top5_freq_list.append(f"| {letter.upper()} -{frequency}%")
            else:
                top5_freq_list.append(f"| {letter.upper()} - {frequency}%")

            top5_freq_dict[letter] = frequency

        return top5_freq_list, top5_freq_dict

    def create_histogram(self):
        histogram = []

        # Populate the histogram with '*' for each letter
        # Start from Z and go backwards #Try not to hard code range , let it adjust based on max letter count
        for y_index in range(len(string.ascii_uppercase), -1, -1):
            line = ''
            for letter in string.ascii_uppercase:  # Use ascii_uppercase for X-axis labels
                count = self.letter_counts.get(letter.lower(), 0)
                # Only print a ' * ' when letter count is greater or equal to y index
                if count >= y_index:
                    line += ' * '
                else:
                    line += '   '

            histogram.append(line)

        return histogram

    def print_histogram_with_Yaxis(self, histogram,  total_width, top5_freq_table):
        line_counter = 0

        for line_hist, letter in zip(histogram, string.ascii_uppercase):
            percentage = self.frequencies.get(letter.lower(), 0)

            # Find starting level for TOP 5 FREQ table
            if 'K' <= letter <= 'Q':
                # Only print if there are lines left in top5_freq_table

                if line_counter < len(top5_freq_table):
                    if percentage > 10:
                        line = "{} | {}-{:.2f}% {:>15s}".format(
                            line_hist, letter, percentage, top5_freq_table[line_counter])
                    else:
                        line = "{} | {}- {:.2f}% {:>15s}".format(
                            line_hist, letter, percentage, top5_freq_table[line_counter])
                    line = " " + line.rjust(total_width)
                    print(line)
                    line_counter += 1
            else:
                # Formatting double-digit percentages
                if percentage > 10:
                    line = "{} | {}-{:.2f}%".format(line_hist,
                                                    letter, percentage)
                else:
                    line = "{} | {}- {:.2f}%".format(line_hist,
                                                     letter, percentage)

                # Reset spaces before line after finishing printing TOP 5 FREQ table to the right of the y-axis

                output_line = " " + line.rjust(total_width)
                print(output_line)

    def X_axis(self, total_width):

        # Print "X axis" using the correct unicode U+2500 (box drawing single horizontal line)
        print('\u2500' * (total_width))

        # Print bottom letters
        print(' ', end=' ')
        for letter in string.ascii_uppercase:
            print(f"{letter}  ", end='')
        print()
