''' 
Advent of Code 2023
Day 10: Pipe Maze
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

def find_element(x, lst):
    for i, row in enumerate(lst):
        try:
            return (i, row.index(x))
        except:
            pass

def arround_ellement(cor, lst):
    print("the cor is:", cor)
    for n in range(-1,2):
        print(cor[0], cor[1]+n)
        print(cor[0]+n, cor[1])


###########################
# part 1
content = single_char_list(read_file('test.txt'))

# find index of S
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# S will have exactly two pipes connecting to it, and is assumed to connect back to those two pipes

cor_s = find_element("S", content)
arround_ellement(cor_s, content)





# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
