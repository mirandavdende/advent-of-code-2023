''' 
Advent of Code 2023
Day 1: Trebuchet?!
'''

# Open file and read content
f = open('test2.txt', 'r')
lines = f.readlines()
f.close()

# remove new lines
content = []
for l in lines:
	content.append(l.replace("\n", ""))

# extract first and last number and add togehter 
total_1 = 0
for string in content:
  num = ""
  for letter in string:
    if letter.isdigit():
      num = num + letter
  total_1 = total_1 + int(num[0]+num[len(num)-1])
print("The solution for the first part of puzzel is:", total_1)

# defenitions for the second part of the puzzel
def replace_number(number):
  ''' Repleces a word with a digit'''
  if number == "one":
    number = 1
  elif number == "two":
    number = 2
  elif number == "three":
    number = 3
  elif number == "four":
    number = 4
  elif number == "five":
    number = 5
  elif number == "six":
    number = 6
  elif number == "seven":
    number = 7
  elif number == "eight":
    number = 8
  elif number == "nine":
    number = 9
  return str(number)

def first_last(string):
  ''' Extract the first and the last number of the string in writen or in digit form'''
  reeks = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  # First number of the string
  first_number = ""
  lowest_index = 1000
  for r in reeks:
    index = string.find(r)
    if index != -1 and index < lowest_index:
      lowest_index = index
      first_number = r
  first_number = replace_number(first_number)
  # Last number of the string
  last_number = ""
  highest_index = 0
  for r in reeks:
    index = string.rfind(r)
    if index != -1 and index >= highest_index:
      highest_index = index
      last_number = r
  last_number = replace_number(last_number)
  print(string, first_number, last_number, (first_number+last_number))
  return (first_number+last_number)

total_2 = 0
for string in content:
  #print(first_last(string))
  total_2 = total_2 + int(first_last(string))
print("The solution for the second part of puzzel is:", total_2)
