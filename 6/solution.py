''' 
Advent of Code 2023
Day 6: Wait For It
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

# Part 1: Ways to win the race
# Your toy boat has a starting speed of zero millimeters per millisecond. 
# For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.

race_dict = dict()
for line in content:
    line_split = line.split()
    for element in line_split:
        if not element.isdigit():
            key = element
        else:
            if key in race_dict:
                race_dict[key].append(element)
            else:
                race_dict[key] = [element]

total = 0
for race in range(len(race_dict["Time:"])):
    wins = 0
    # print("This is race", race)
    time = int(race_dict["Time:"][race])
    for millisec in range(time):
        hold_time = millisec
        distance_raced = hold_time * (time - hold_time)
        if distance_raced > int(race_dict["Distance:"][race]):
            wins += 1
    # print("Wins for race", race, "is:", wins) 
    if total == 0:
        total = wins
    else:
        total = total * wins

print("The solution for part one is:", total)

# Part 2: There is only one race
race_dict = dict()
for line in content:
    line_split = line.split(":")
    for element in line_split:
        element = element.replace(" ", "")
        if not element.isdigit():
            key = element
        else:
            race_dict[key] = [int(element)]

total = 0
wins = 0
time = int(race_dict["Time"][0])
for millisec in range(time):
    hold_time = millisec
    distance_raced = hold_time * (time - hold_time)
    if distance_raced > int(race_dict["Distance"][0]):
         wins += 1

print("The solution for part one is:", wins)