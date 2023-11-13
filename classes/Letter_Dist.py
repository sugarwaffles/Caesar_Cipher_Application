#Name: Wilfred Djumin
#Class: DAAA/FT/2B05
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
        # If the list is currently empty
        if self.headNode is None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode.data[1] > self.headNode.data[1]:
            self.__appendToHead(newNode)
            return

        # Check if it is going to be inserted between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode is not None:
            if newNode.data[1] > rightNode.data[1] or (
                newNode.data[1] == rightNode.data[1] and newNode.data[0] < rightNode.data[0]
            ):
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        # Once we reach here, it must be added at the tail
        leftNode.nextNode = newNode
    # Iterates through the nodes to     
    def get_sorted_list(self):
        result = []
        current_node = self.headNode
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.nextNode
        return result

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
        for letter, frequency in sorted(self.frequencies.items(), key=lambda x: (-x[1], x[0])):
            sorted_freq.insert(SortedList.Node((letter, frequency)))

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
        
    

















