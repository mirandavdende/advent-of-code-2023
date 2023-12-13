''' 
Advent of Code 2023
Day 13: Point of Incidence
'''

def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    content = []
    for l in lines:
        #if l != '\n':
            content.append(l.replace("\n", " "))
    content.append(" ")
    return content

def single_char_list(input):
    new_content = []
    pattern = []
    for line in input:
        char_list = []
        if len(line) == 1:
            new_content.append(pattern)
            pattern = []
        else:
            for char in line:
                if char != ' ':
                    char_list.append(char)
            pattern.append(char_list)
        
    return new_content

def flip(input):
    flipped = []
    for x in range(len(input[0])): # x = col number
        col = []
        for y in range(len(input)): # y = row number
            col.append(input[y][x])
        flipped.append(col)
    return flipped

def reflect(input):
    reflection = []
    for n in range(len(input)-1):
        if input[n] == input[n+1]:
            reflection.append(n)
    lenght = len(input)
    summarize = 0
    if len(reflection) == 0:
        return summarize
    else:
        for n in reflection:
            count = 0
            for x in range(1, (lenght - 1)-n):
                if input[n-x] == input[n+1+x]:
                    count += 1
                else:
                    break 
            if count == n or count == (lenght-n-2):
                summarize = n + 1
    return summarize

def summarize_patterns(input):
    total = 0
    for block in input:
        horizontal = reflect(block) * 100
        vertical = reflect(flip(block))
        total = total + vertical + horizontal
    return total

# Part 1: reflections
content = single_char_list(read_file('input.txt'))
total = summarize_patterns(content)
print("The solution for part one is:", total) # 37561

# Part 2: 