''' 
Advent of Code 2023
Day 18: Lavaduct Lagoon 
'''
import copy
import sys
sys.setrecursionlimit(1000000)

def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def new_coordinate(cor, movement):
    y_move = 0
    x_move = 0
    match movement[0]:
        case "L":
            x_move = - movement[1]
        case "R":
            x_move = movement[1]
        case "U":
            y_move = - movement[1]
        case "D":
            y_move = movement[1]
    new_coordinate = (cor[0] + y_move , cor[1] + x_move)
    return new_coordinate

def coordinate_list(input):
    coordinate_list = [(150,100)]
    # coordinate_list = [(0,0)]
    count = 0
    for line in input:
        split_line = line.split(" ")
        next_coordinate = new_coordinate(coordinate_list[count], (split_line[0], int(split_line[1])))
        coordinate_list.append(next_coordinate)
        count += 1
    return coordinate_list

def Shoelace_method(input):
    a1 = 0
    a2 = 0
    for n in range(len(input)-1):
        print(input[n], input[n+1])
        a1 = a1 + (input[n][1]) * (input[n+1][0] +1)
        a2 = a2 + (input[n][0]) * (input[n+1][1] +1)
    a = (a1 -a2) * 0.5
    return a

def draw_grid(input):
    max_y = max( [int(x[0]) for x in input ])
    max_x = max( [int(x[1]) for x in input ])
    grid = []
    row = []
    for x in range(max_x+1):
        row.append(".")
    for y in range(max_y+1):
        grid.append(row.copy())
    last = input[0]
    for cor in input:
        grid[cor[0]][cor[1]]= "#"
        dif_x = (cor[1] - last[1])
        dif_y = (cor[0] - last[0])
        if dif_x > 0:
            for x in range(dif_x):
                grid[last[0]][last[1]+x]= "#"
        if dif_x < 0:
            for x in range(dif_x, 0):
                grid[last[0]][last[1]+x]= "#"
        if dif_y > 0:
            for y in range(dif_y):
                grid[last[0]+y][last[1]]= "#"
        if dif_y < 0:
            for y in range(dif_y, 0):
                grid[last[0]+y][last[1]]= "#"
        last = cor
    return grid

def flood_fill(input, cor):
    if cor[0] > 0 and cor[1] > 0 and cor[0] < len(input) and cor[1] < len(input[0]) and input[cor[0]][cor[1]] == ".":
        input[cor[0]][cor[1]] = "#"
        flood_fill(input, (cor[0], cor[1]+1))
        flood_fill(input, (cor[0]+1, cor[1]))
        flood_fill(input, (cor[0], cor[1]-1))
        flood_fill(input, (cor[0]-1, cor[1]))

def tims_draw_grid(cors):
    # Collect dimensions
    minX = min([cor[1] for cor in cors])
    minY = min([cor[0] for cor in cors])
    maxX = max([cor[1] for cor in cors])
    maxY = max([cor[0] for cor in cors])
    width = maxX - minX + 1
    height = maxY - minY + 1

    # Generate image
    image = [['.' for _ in range(width)] for _ in range(height)]
    for i in range(0, len(cors)-1):
        start, end = cors[i:i+2]
        y, x = start
        dy = clamp(end[0] - start[0])
        dx = clamp(end[1] - start[1])
        while x != end[1]+dx or y != end[0]+dy:
            image[y-minY][x-minX] = "#"
            x += dx
            y += dy
    return image

def clamp(value):
    if value == 0:
        return 0
    if value > 0:
        return 1
    return -1

# Part 1: how many cubic meters of lava could it hold?
content = read_file('input.txt')
coordinates = (coordinate_list(content))
# grid = tims_draw_grid(coordinates)
# flood_fill(grid, (1,86))

grid = draw_grid(coordinates)
flood_fill(grid, (15,144))

total = 0
for line in grid:
    total += line.count("#")
print("The solution for part one is:", total)

# Part 2: 

# Each hexadecimal code is six hexadecimal digits long. 
# The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. 
# The last hexadecimal digit encodes the direction to dig: 
# 0 means R, 1 means D, 2 means L, and 3 means U.


# Test: 952408144115 