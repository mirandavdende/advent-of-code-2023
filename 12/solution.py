''' 
Advent of Code 2023
Day 12: Hot Springs
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
        digit_list = []
        char_list = []
        for char in line:
            if char.isdigit():
                digit_list.append(char)
            elif char != ' ' and char != ",":
                char_list.append(char)
        new_content.append([char_list]+[digit_list])
    return new_content

from itertools import permutations

def generate_possibilities(input):
    print(input)
    row = input[0]
    l = len(input[0])
    group_sizes = [ int(n) for n in input[1].split(",")]
    num_hash = sum(group_sizes)
    num_dot = l - num_hash

    print(row, l, group_sizes, num_hash, num_dot)
    
    # all_permutations = list(permutations("#" * num_hash + "." * num_dot))
    # print(all_permutations)



# Part 1: calculte the the number of possible arrangements
content = (read_file('test.txt'))
for line in content:
    line = line.split()
    generate_possibilities(line)


# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangements