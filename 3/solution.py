''' 
Advent of Code 2023
Day 3: Gear Ratios
'''

# Open file and read content
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# remove new lines
content = []
for l in lines:
	content.append(l.replace("\n", "."))

# Part 1: Calculate the sum of any number adjacent to a symbol
# Make a symbol index list
l = 0
symbol_index_list = []
for line in content:
    i = 0
    for x in line:
        if x != ".":
            index = [l,i]
            if not x.isdigit():
                 symbol_index_list.append(index)
        i += 1
    l += 1

# extraxt numbers and check if the number is adjacent to a symbol
number_list = []
sum = 0
l = 0
status = False 
digit_index = [0,0]
for line in content:
    i = 0
    number = ""
    # print("This is line", l, ":", line)
    for digit in line:
        if digit.isdigit():
            digit_index = [l,i]
            # print("index is: ", digit_index)
            if digit_index[0] > 0 and digit_index[1] > 0:
                for y in range(-1,2):  
                    for x in range(-1,2):
                        if [digit_index[0]+x,digit_index[1]+y] in symbol_index_list:
                            status = True 
            elif digit_index[1] > 0:
                for y in range(-1,2):  
                    for x in range(0,2):
                        if [digit_index[0]+x,digit_index[1]+y] in symbol_index_list:
                            status = True 
            number = "".join([number, digit])
        if not digit.isdigit():
            index = [l,i]
            if index[1]-1 == digit_index[1] and status == True:
                 # print("Added number:", number)
                 number_list.append(number)
                 sum = sum + int(number)
                 number = ""
                 status = False 
        if digit == '.':
            number = ""
            status = False 
        i += 1
    l += 1

print("The solution for part one is:", sum)

# Part 2: Gear ratio's - A gear is any * symbol that is adjacent to exactly two part numbers

# Make a gear(*) index list
l = 0
gear_index_list = []
for line in content:
    i = 0
    for x in line:
        if x == "*":
            index = [l,i]
            gear_index_list.append(index)
        i += 1
    l += 1

# extraxt numbers and check if the number is adjacent to a gear
number_list = []
l = 0
status = False 
digit_index = [0,0]
for line in content:
    i = 0
    number = ""
    # print("This is line", l, ":", line)
    for digit in line:
        if digit.isdigit():
            digit_index = [l,i]
            # print("index is: ", digit_index)
            if digit_index[0] > 0 and digit_index[1] > 0:
                for y in range(-1,2):  
                    for x in range(-1,2):
                        if [digit_index[0]+x,digit_index[1]+y] in gear_index_list:
                            status = True 
                            gear_loaction = [digit_index[0]+x,digit_index[1]+y] 
            elif digit_index[1] > 0:
                for y in range(-1,2):  
                    for x in range(0,2):
                        if [digit_index[0]+x,digit_index[1]+y] in gear_index_list:
                            status = True 
                            gear_loaction = [digit_index[0]+x,digit_index[1]+y] 
            number = "".join([number, digit])
        if not digit.isdigit():
            index = [l,i]
            if index[1]-1 == digit_index[1] and status == True:
                 number_list.append([gear_loaction, int(number)])
                 # print("Added number:", number, "for location:", gear_loaction)
                 number = ""
                 status = False 
        if digit == '.':
            number = ""
            status = False 
        i += 1
    l += 1

number_dict = {}
for gear in number_list:
    key = str(gear[0])
    if key in number_dict:
        number_dict[key].append(gear[1])
    else:
        number_dict[key] = [gear[1]]

total = 0
for numbers in number_dict.values():
    if len(numbers) == 2:
        gear_ratio = numbers[0] * numbers[1]
        total += gear_ratio

print("The solution for part two is:", total) 