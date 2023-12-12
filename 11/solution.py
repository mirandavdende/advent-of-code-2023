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

def expanding_coordinates(input):
    cor_rows = []
    rows = 0
    for line in input: # rows
        if all(i == "." for i in line):
            cor_rows.append(rows)
        rows +=1
    cor_cols = []
    cols = 0
    for x in range(len(input[0])): # x = col number
        col = []
        for y in range(len(input)): # y = row number
            col.append(input[y][x])
        if all(i == "." for i in col): 
            cor_cols.append(cols)
        cols += 1
    exp_cor = [cor_rows] +  [cor_cols]
    return exp_cor

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

def calulate_distance_2(input, cor_exp):
    expand_distance = 999999
    cor_rows = cor_exp[0]
    cor_cols = cor_exp[1]
    distance_list = []
    for x in range(len(input)):
        cor1 = input[x]
        for n in range(x+1, len(input)):
            cor2 = input[n]
            distance = abs(cor1[0] - cor2[0]) + abs(cor1[1] - cor2[1])
            # rows tussenliggende nummers tussen 1 en 0 --> 1 geen expand
            for row in range(cor1[0], cor2[0]):
                if row in cor_rows:
                    distance += expand_distance
            # col: tussenliggende nummers tussen 3 en 7 --> expand op 5
            if cor1[1] < cor2[1]:
                for col in range(cor1[1], cor2[1]):
                    if col in cor_cols:
                        distance += expand_distance
            else:
                for col in range(cor2[1], cor1[1]):
                    if col in cor_cols:
                        distance += expand_distance
            distance_list.append(distance)
            # print(cor1, cor2, distance)
    return distance_list

# Part 1: Farthest position of the loop
# empty space (.) and galaxies (#)
content = single_char_list(read_file('input.txt'))
# exapand galaxy
expand_content = expand_galaxy(content)
# Get coordinates of all galaxies
cor_content = get_coordinates(expand_content)
# What is the sum of these lengths?
distance_list = calulate_distance(cor_content)
print("The solution for part one is:", sum(distance_list))

# Part 2: Galaxies expand by 1000000
# get coordinates of galaxies
cor_gal = (get_coordinates(content))
# get rows and columns that expand
cor_exp = (expanding_coordinates(content))
# calculate distance and sum
distance_list = calulate_distance_2(cor_gal, cor_exp)
print("The solution for part two is:", sum(distance_list)) 



