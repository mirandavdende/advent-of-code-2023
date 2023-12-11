''' 
Advent of Code 2023
Day 11: Cosmic Expansion
'''
import copy

def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    content = []
    for l in lines:
        if l != '\n':
            content.append(l.replace("\n", " "))
    return content

def single_char_list(input):
    new_content = []
    for line in input:
        char_list = []
        for char in line:
            if char != ' ':
                char_list.append(char)
        new_content.append(char_list)
    return new_content

def expand_galaxy(input):
    # any rows or columns that contain no galaxies should all actually be twice as big.
    new_input = []
    for line in input: # rows
        new_input.append(line)
        if all(i == "." for i in line): # add same line afer current line
            new_input.append(line.copy())
    output = copy.deepcopy(new_input)
    expand = 0
    for x in range(len(new_input[0])): # x = col number
        col = []
        for y in range(len(new_input)): # y = row number
            col.append(new_input[y][x])
        if all(i == "." for i in col): # add same line afer current line
            for n in range(len(new_input)):
                output[n].insert((x + expand), ".")
            expand += 1
    return output

def get_coordinates(input):
    locations = []
    for row in range(len(input)): # rows
        for element in range(len(input[row])):
            if input[row][element] == "#":
                locations.append([row,element])
    return locations

def calulate_distance(input):
    # shortest path between every pair of galaxies
    # Only count each pair once
    # using only steps that move up, down, left, or right exactly one . or # at a time. 
    # The shortest path between two galaxies is allowed to pass through another galaxy.
    distance_list = []
    for x in range(len(input)):
        cor1 = input[x]
        for n in range(x+1, len(input)):
            cor2 = input[n]
            distance = abs(cor1[0] - cor2[0]) + abs(cor1[1] - cor2[1])
            distance_list.append(distance)
            # print(cor1, cor2, distance)
    return distance_list

# Part 1: Farthest position of the loop
# empty space (.) and galaxies (#)
content = single_char_list(read_file('test.txt'))
# exapand galaxy
expand_content = expand_galaxy(content)
# Get coordinates of all galaxies
cor_content = get_coordinates(expand_content)
# What is the sum of these lengths?
print(sum(calulate_distance(cor_content))) #9274989

# Test: there are 36 pairs of galaxies, the sum of the steps is 374.
