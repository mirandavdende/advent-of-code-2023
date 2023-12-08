''' 
Advent of Code 2023
Day 8: Haunted Wasteland
'''
# Open file and read content
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# remove new lines
content = []
for l in lines:
    if l != '\n':
        content.append(l.replace("\n", " "))

# Part 1: Follow the instructions

# Make a instruction list
instructions = []
for letter in content[0]:
    if letter.isalpha():
        instructions.append(letter)
del content[0]

# Make a map dataframe
clean_content = []
for line in content:
    line_list = []
    for element in line.split():
        if element != '=':
            element = element.replace('(', '')
            element = element.replace(')', '')
            element = element.replace(',', '')
            line_list.append(element)
    clean_content.append(line_list)

import pandas as pd
df = pd.DataFrame(columns=['start', 'L', 'R'])

for n in clean_content:
    df.loc[len(df.index)] = [n[0], n[1], n[2]] 

# Follow instructions in map to ZZZ
steps = 0
position = 'AAA'
found = False
while not found:
    for instruction in instructions:
        map = df.loc[df['start'] == position]
        position = (map[instruction].to_string(index=False))
        steps += 1
        if position == 'ZZZ':
            found = True
            break

print("The solution for part one is:", steps)

# Part 2: start at every node that ends with A, and end if every node ends with Z 

start_str = 'A'
positions = []
for line in range(len(df)):
    position = df['start'].iloc[line]
    if position[2] == start_str:
        positions.append(position)

end_str = 'Z'
found = False
step_list = []
for position in positions:
    steps = 0
    found = False
    while not found:
        for instruction in instructions:
            map = df.loc[df['start'] == position]
            position = (map[instruction].to_string(index=False))
            steps += 1
            if position[2] == end_str:
                found = True
                # print("End is:", position, "in", steps, "steps")
                step_list.append(steps)

# least common multiple
from math import gcd
def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def find_lcm(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result
result_lcm = find_lcm(step_list)

print("The solution for part two is:", result_lcm)
# fout: 20803 (too low), 33458567957100 (too high)
