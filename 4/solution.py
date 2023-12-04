''' 
Advent of Code 2023
Day 4: Scratchcards
'''

# Open file and read content
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# remove new lines
content = []
for l in lines:
	content.append(l.replace("\n", " "))

# Part 1: Winning numbers
sum = 0
for card in content:
    card = card.split(":")
    # print("This is", card[0])
    numbers = card[1].split("|")
    winning_numbers = numbers[0].split(" ")
    while("" in winning_numbers):
        winning_numbers.remove("")
    my_numbers = numbers[1].split(" ")
    while("" in my_numbers):
        my_numbers.remove("")      
    wins = 0
    for n in my_numbers:
         if n in winning_numbers:
              wins += 1
    # print("Ammount of wins:", wins)
    if wins > 0:
        points = 1
        for x in range(1, wins):
                points = points * 2
    else:
         points = 0
    # print("Ammount of points:", points)
    sum = sum + points

print("The solution for part one is:", sum)

# Part 2: Multiplying Scratchcards
cards_list = [1] * len(content)

sum = 0
card_n = 0
for card in content:
    card_n += 1
    card = card.split(":")
    numbers = card[1].split("|")
    winning_numbers = numbers[0].split(" ")
    while("" in winning_numbers):
        winning_numbers.remove("")
    my_numbers = numbers[1].split(" ")
    while("" in my_numbers):
        my_numbers.remove("")      
    wins = 0
    for n in my_numbers:
         if n in winning_numbers:
              wins += 1
    for w in range(wins):
         cards_list[card_n+w] = cards_list[card_n+w] + (1*cards_list[card_n-1])

total = 0
for number in cards_list:
     total += number

print("The solution for part two is:", total) 
