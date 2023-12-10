''' 
Advent of Code 2023
Day 9: Mirage Maintenance
'''
from helpers.files import read_file

def make_number_lists(input):
    number_lists = []
    for line in input:
        number_list = []
        for number in line.split():
            number_list.append(int(number))
        number_lists.append(number_list)
    return number_lists

def make_difference_list(list):
    difference_list = []
    while True:
        difference_list.append(list)
        if all(i == 0 for i in list):
            break
        else:
            list = [b - a for a, b in zip(list, list[1:])]    
    return difference_list

def prediction_extrapolated_values(lists):
    while lists:
        last_list = lists.pop()
        try:
            next_value = lists[-1][-1] + last_list[-1]
            lists[-1].append(next_value)
        except IndexError:
            break
    return next_value

def history_extrapolated_values(lists):
    while lists:
        last_list = lists.pop()
        try:
            first_value = lists[-1][0] - last_list[0]
            lists[-1].insert(0, first_value)
        except IndexError:
            break
    return first_value

content = read_file('9/input.txt')
number_lists = make_number_lists(content)

total = 0
for number_list in number_lists:
    difference = make_difference_list(number_list)
    total = total + prediction_extrapolated_values(difference)

print("The solution for part one is:", total)

total = 0
for number_list in number_lists:
    difference = make_difference_list(number_list)
    total = total + history_extrapolated_values(difference)

print("The solution for part two is:", total)