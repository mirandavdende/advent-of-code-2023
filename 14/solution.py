''' 
Advent of Code 2023
Day 14: Parabolic Reflector Dish 
'''

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

def flip_columns(input):
    flipped = []
    for x in range(len(input[0])): # x = col number
        col = []
        for y in range(len(input)): # y = row number
            col.append(input[y][x])
        flipped.append(col)
    return flipped

def slide_left(input):
    for x in range(len(input)):
        moved = True
        while moved:
            moved = False
            for y in range(1, len(input[x])):
                if input[x][y] == "O":
                    if input[x][y-1] == ".":
                        input[x][y] = "."
                        input[x][y-1] = "O"
                        moved = True
    return input

def slide_right(input):
    for x in range(len(input)):
        moved = True
        while moved:
            moved = False
            for y in range(len(input[x])-2, -1, -1):
                if input[x][y] == "O":
                    if input[x][y+1] == ".":
                        input[x][y] = "."
                        input[x][y+1] = "O"
                        moved = True
    return input

def slide_north(input): # up
    flipped_input = flip_columns(input)
    flipped_input_slide = slide_left(flipped_input)
    new_input = flip_columns(flipped_input_slide)
    return new_input

def slide_west(input): # left
    input_slide = slide_left(input)
    return input_slide

def slide_south(input): # down
    flipped_input = flip_columns(input)
    flipped_input_slide = slide_right(flipped_input)
    new_input = flip_columns(flipped_input_slide)
    # new_input = slide_right(input)
    return new_input

def slide_east(input): # right
    new_input = slide_right(input)
    return new_input

def cycle(input):
    # Cycle: north, then west, then south, then east. 
    # calculate the total load on the north support beams after 1000000000 cycles.
    for n in range(1000000000):
        print(n)
        input = slide_north(input)
        # print("N")
        # for line in input:
        #     print(line)
        input = slide_west(input)
        # print("W")
        # for line in input:
        #     print(line)
        input = slide_south(input)
        # print("S")
        # for line in input:
        #     print(line)
        input = slide_east(input)
        # print("E")
        # for line in input:
        #     print(line)
    return input

def load(input):
    load = len(input)
    total = 0
    for line in input:
        sum_line = line.count("O") * load
        load -= 1
        total = total + sum_line
    return total

# Part 1: Load on the north beam
content = single_char_list(read_file('test.txt'))
content_north = slide_north(content)
load_input = load(content_north)
print("The solution for part one is:", load_input) # 107053

# Part 2: Cycle: north, west, south, east for 1000000000 cycles and calculate the total load
cycles_content = cycle(content)
load_input = load(cycles_content)
print("The solution for part two is:", load_input) 
# Test = 64
