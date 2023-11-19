#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
import string

# Parent Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def get_letter(self):
        return self.data[0]

    def get_frequency(self):
        return self.data[1]

# Child Class LetterNode
class LetterNode(Node):
    def __lt__(self, other):
        return self.data[1] > other.data[1] or (self.data[1] == other.data[1] and self.data[0] < other.data[0])
    def get_data(self):
        return self.data
# SortedList class
class SortedList:
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

        if self.headNode is None:
            self.headNode = newNode
            return

        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode is not None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        leftNode.nextNode = newNode

    def __str__(self):
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
        current_node = self.headNode
        current_index = 0

        while current_node is not None and current_index < index:
            current_node = current_node.nextNode
            current_index += 1

        if current_index == index and current_node is not None:
            return current_node.get_data()

        return None
    # Inside the SortedList class
    def get_letter_at_index(self, index):
        data = self.get_data_at_index(index)
        return data[0] if data else None
    
    def get_sorted_list(self):
        sorted_list = []
        node = self.headNode
        while node is not None:
            sorted_list.append(node.get_data())
            node = node.nextNode
        return sorted_list

class LetterFrequencyDistribution:
    def __init__(self, filename):
        self.filename = filename
        self.letter_counts, self.frequencies = self.calculate_letter_counts_and_frequencies()
        self.sorted_frequencies = self.sort_frequencies()
    def calculate_letter_counts_and_frequencies(self):
        with open(self.filename, 'r') as file:
            text = file.read().lower()
            letter_counts = {letter: text.count(letter) for letter in string.ascii_lowercase}
            total_letters = sum(letter_counts.values())
            frequencies = {k: round(v / total_letters * 100, 2) for k, v in letter_counts.items()}
        return letter_counts, frequencies    
        
    def analyze_file(self):
            
            # Print top 5 frequencies
            top5_freq_table = self.calculate_top5_frequencies()

            # Total width represents the num of characters(space in this case) to fill the missing spaces (to the left of the str) which will be used for the y-axis creation
            total_width = 80

            # Create a list to store the histogram
            histogram = self.create_histogram()

            # Print the histogram
            self.print_histogram(histogram,total_width, top5_freq_table)
            
            #Print the X-axis
            self.X_axis(total_width)
            
    def sort_frequencies(self):
        sorted_freq = SortedList()
        for letter, frequency in self.frequencies.items():
            sorted_freq.insert(LetterNode([letter, frequency]))
            
        return sorted_freq
    
    def calculate_top5_frequencies(self):
        
        top5_freq_table = []
        #Appending the headers of the TOP 5 FREQ table
        top5_freq_table.append("TOP 5 FREQ")
        top5_freq_table.append("-" * 11)
    
        # Iterate over the first five nodes in the sorted list
        current_node = self.sorted_frequencies.headNode
        for _ in range(5):
            if current_node is None:
                break
            letter, frequency = current_node.data
            if frequency > 10:
                top5_freq_table.append(f"| {letter.upper()} -{frequency}%")
            else:
                top5_freq_table.append(f"| {letter.upper()} - {frequency}%")
            current_node = current_node.nextNode

        return top5_freq_table
    
    def create_histogram(self):
        histogram = []

        # Populate the histogram with '*' for each letter
        for y_index in range(len(string.ascii_uppercase), -1, -1):  # Start from Z and go backwards #Try not to hard code range , let it adjust based on max letter count
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

    def print_histogram(self, histogram,  total_width, top5_freq_table):
        line_counter = 0

        for line_hist, letter in zip(histogram, string.ascii_uppercase):
            percentage = self.frequencies.get(letter.lower(), 0)

            # Find starting level for TOP 5 FREQ table
            if 'K' <= letter <= 'Q':
                # Only print if there are lines left in top5_freq_table
                
                if line_counter < len(top5_freq_table):
                    if percentage >10:
                        line = "{} | {}-{:.2f}% {:>15s}".format(line_hist, letter, percentage, top5_freq_table[line_counter])
                    else:
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
                
    def X_axis(self,total_width):
        
        # Print "X axis" using the correct unicode U+2500 (box drawing single horizontal line)
        print('\u2500' * (total_width))

        # Print bottom letters
        print(' ', end=' ')
        for letter in string.ascii_uppercase:
            print(f"{letter}  ", end='')
        print()
        
    

















