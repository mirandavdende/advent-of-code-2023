''' 
Advent of Code 2023
Day 2: Cube Conundrum
'''
# Open file and read content
f = open('input.txt', 'r')
lines = f.readlines()
f.close()
# remove new lines
content = []
for l in lines:
	content.append(l.replace("\n", ""))

# Part 1: there are max 12 red cubes, 13 green cubes, and 14 blue cubes. 
def total_good_games(content):
  ''' Calculates the sum of the ammount of games that are good games, with equal or less than 12 red cubes, 13 green cubes, and 14 blue cubes'''
  total = 0
  for game in content:
    game = game.split(":")
    game_n = (game[0].split(" "))[1]
    # print("This is game: ", game_n)
    good_game = True
    hands = game[1].split(";")
    for hand in hands:
      hand = hand.split(",")
      for color in hand:
        if "red" in color:
          n = int(color.replace('red', ''))
          # print("Red:", n)
          if n > 12:
            # print(color, "too much")
            good_game = False
            break
        elif "green" in color:
          n = int(color.replace('green', ''))
          # print("Green:", n)
          if n > 13:
            # print(color, "too much")
            good_game = False
            break
        elif "blue" in color:
          n = int(color.replace('blue', ''))
          # print("Blue:", n)
          if n > 14:
            # print(color, "too much")
            good_game = False
            break
    # print(good_game)
    if good_game == True:
      total = total + int(game_n)
  return total

print("Awnser part 1: ", total_good_games(content))

# Part 2: what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

def min_cubes(content):
  '''  '''
  total = 0
  for game in content:
    game = game.split(":")
    game_n = (game[0].split(" "))[1]
    # print("This is game: ", game_n)
    
    red = 0
    green = 0
    blue = 0

    hands = game[1].split(";")
    for hand in hands:
      # print(hand)
      hand = hand.split(",")
      for color in hand:
        if "red" in color:
          n = int(color.replace('red', ''))
          # print("Red:", n)
          if red < n:
            red = n
        elif "green" in color:
          n = int(color.replace('green', ''))
          # print("Green:", n)
          if green < n:
            green = n
        elif "blue" in color:
          n = int(color.replace('blue', ''))
          # print("Blue:", n)
          if blue < n:
            blue = n

    #print("Min red cubes: ", red)
    #print("Min green cubes: ", green)
    #print("Min blue cubes: ", blue)
    power = (red * green * blue) # 48, 12, 1560, 630, and 36, 
    total = total + power
  return total

print("Awnser part 2: ", min_cubes(content))