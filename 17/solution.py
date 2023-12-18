''' 
Advent of Code 2023
Day 17: Clumsy Crucible
'''

def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def calculte_next_steps(input):
    x_cor = 0
    y_cor = 0
    print(input[y_cor][x_cor])
    # 3 steps down
    down = 0
    for y in range(1,4):
        down = down + int(input[y_cor + y][x_cor])
    print(down)
    # 3 steps left
    left = 0 
    for x in range(1,4):
        left = left + int(input[y_cor][x_cor + x])
    print(left)
    # 2 steps left, 1 step down
    left_down = 0

# Part 1: best way to get the crucible from the lava pool to the machine parts factory
content = read_file('test.txt')

for line in content:
    print(line)

calculte_next_steps(content)

# Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block.

# The starting point, the lava pool, is the top-left city block
# the destination, the machine parts factory, is the bottom-right city block.

# it can move at most three blocks in a single direction before it must turn 90 degrees left or right
# after entering each city block, it may only turn left, continue straight, or turn right.

# This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.