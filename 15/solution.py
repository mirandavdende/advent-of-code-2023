''' 
Advent of Code 2023
Day 15: Lens Library
'''
def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def calculate_block(input):
    result = 0
    for i in input:
        # Determine the ASCII code for the current character of the string. --> ord(value)
        # Increase the current value by the ASCII code you just determined.
        result = result + ord(i)
        # Set the current value to itself multiplied by 17.
        result = result * 17
        # Set the current value to the remainder of dividing itself by 256.
        result = result % 256
    return result

def calculate_total(input):
    total = 0
    input = input.split(',')
    for block in input:
        result = calculate_block(block)
        total = result + total
    return total

# Part 1:
content = read_file('input.txt')
print("The solution for part one is:", calculate_total(content[0])) # 517551




# Determine the ASCII code for the current character of the string. --> ord(value)
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

# In this example, the sum of these results is 1320