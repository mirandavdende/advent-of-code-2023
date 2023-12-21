''' 
Advent of Code 2023
Day 21: Step Counter
'''

def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def find_start(input):
    row = 0
    for line in input:
        col = 0
        for char in line:
            if char == "S":
                start = (col, row)
            col += 1
        row += 1
    return [start]

def possible_steps(coordinates, input):
    # starting position (S), garden plots (.), and rocks (#)
    new_coordinates = []
    for cor in coordinates:
        # north
        north = (cor[0]-1, cor[1])
        if not north[0] < 0 or not north[1] < 0:
            if input[north[0]][north[1]] == "." or input[north[0]][north[1]] == "S":
                # print("possible step north", north)
                new_coordinates.append(north)
        # south
        south = (cor[0]+1, cor[1])
        if not south[0] < 0 or not south[1] < 0:
            if input[south[0]][south[1]] == "." or input[south[0]][south[1]] == "S":
                # print("possible step south", south)
                new_coordinates.append(south)
        # east
        east = (cor[0], cor[1]+1)
        if not east[0] < 0 or not east[1] < 0:
            if input[east[0]][east[1]] == "." or input[east[0]][east[1]] == "S":
                # print("possible step east", east)
                new_coordinates.append(east)
        # west
        west = (cor[0], cor[1]-1)
        if not west[0] < 0 or not west[1] < 0:
            if input[west[0]][west[1]] == "." or input[west[0]][west[1]] == "S":
                # print("possible step west", west)
                new_coordinates.append(west)
    # Remove dublicates
    coordinates = []
    for cor in new_coordinates:
        if cor not in coordinates:
            coordinates.append(cor)
    return coordinates

def walk(start, input):
    steps = 64
    coordinates = start
    for step in range(steps):
        # print("this is step", step, len(coordinates))
        coordinates = possible_steps(coordinates, input)
    return len(coordinates)

# Part 1: 64 steps
content = read_file('input.txt')
start = find_start(content)
print("The solution for part one is:", walk(start, content)) # 3809
# Example: 6 steps, 16 garden plots.

# Part 2: 