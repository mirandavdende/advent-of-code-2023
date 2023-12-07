''' 
Advent of Code 2023
Day 7: Camel Cards
'''

# Open file and read content
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# remove new lines
content = []
for l in lines:
    content.append(l.replace("\n", " "))

# Part 1: total winnings based on ranks 

def replace_letter(input):
    # A(14), K(13), Q(12), J(11), T(10), 9, 8, 7, 6, 5, 4, 3, or 2.
    if input.isdigit():
        output = input
    else:
        if input == 'A':
            output = 14
        elif input == 'K':
            output = 13
        elif input == 'Q':
            output = 12
        elif input == 'J':
            output = 11
        elif input == 'T':
            output = 10
    return int(output)

# Score hands for kind of hand
hand_order = []
for row in content:
    hand_bid = row.split()
    hand = hand_bid[0]
    bid = int(hand_bid[1])
    # print("this is hand:", hand, "with a bid of:", bid)
    hand_count = []
    if hand == len(hand)*hand[0]:
        result = 7 # "Five of a kind"
    else:
        for n in range(len((hand))):
            hand_count.append(hand.count(hand[n]))
            #print(hand[n], "komt", hand.count(hand[n]), "keer voor")
        if sum(hand_count) == 5:
            result = 1 # "High card"
        elif sum(hand_count) == 7:
            result = 2 #"One pair"  
        elif sum(hand_count) == 9:
            result = 3 #"Two pair"    
        elif sum(hand_count) == 11:
            result = 4 #"Three of a kind"   
        elif sum(hand_count) == 13:
            result = 5 #"Full house"                
        elif sum(hand_count) == 17:
            result = 6 #"Four of a kind"
    # print("this is hand:", hand, "with a result of:", result)
    hand_order.append([result, hand, bid])
  
# Check with hand in a specific hand score is higher
new_hand_order = []
for n in range(1,8):# numbers 1 t/m 7
    # print(n)
    temp_hands = []
    for hand in hand_order: 
        if hand[0] == n:
            temp_hands.append(hand)
    if temp_hands != []:
        #print(temp_hands)
        n = len(temp_hands)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                # print(temp_hands[j][1], temp_hands[j + 1][1])
                for l in range(len(temp_hands[j][1])):
                    # print(temp_hands[j][1][l], temp_hands[j + 1][1][l])
                    if replace_letter(temp_hands[j][1][l]) > replace_letter(temp_hands[j + 1][1][l]):
                        temp_hands[j], temp_hands[j + 1] = temp_hands[j + 1], temp_hands[j]
                        break
                    elif replace_letter(temp_hands[j][1][l]) < replace_letter(temp_hands[j + 1][1][l]):
                        break
        new_hand_order += temp_hands           
# print(new_hand_order)

# Calculate the total
total = 0
for n in range(len(new_hand_order)):
    # print(new_hand_order[n][1])
    # print(int(new_hand_order[n][2]), (n+1))
    # print(int(new_hand_order[n][2]) * (len(new_hand_order) - n))
    total = total + (int(new_hand_order[n][2]) * (n+1))

print("The solution for part one is:", total)
# Fout: 256447922, 254014885






# Part 2
def replace_letter_2(input):
    # A(14), K(13), Q(12), J(1), T(10), 9, 8, 7, 6, 5, 4, 3, or 2.
    if input.isdigit():
        output = input
    else:
        if input == 'A':
            output = 14
        elif input == 'K':
            output = 13
        elif input == 'Q':
            output = 12
        elif input == 'J':
            output = 1
        elif input == 'T':
            output = 10
    return int(output)

# Score hands for kind of hand
card_list = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
hand_order = []
for row in content:
    hand_bid = row.split()
    hand = hand_bid[0]
    bid = int(hand_bid[1])
    # print("this is hand:", hand, "with a bid of:", bid)
    hand_count = []
    hand_count_2 = []
    sum_score = 0
    if 'J' in hand:
        for n in range(len((hand))):
            hand_count_2.append(hand.count(hand[n]))
        sum_score = sum(hand_count_2)
        # print(hand, "this has a J, the score is:", sum_score)

        for card in card_list:
            new_hand = hand.replace("J", card)
            for n in range(len((new_hand))):
                hand_count.append(new_hand.count(new_hand[n]))
            score = sum(hand_count)
            # print(new_hand, "has a score of", score)
            if score > sum_score:
                # print(new_hand, "has a higer score of", score)
                sum_score = score
            hand_count = []
        # print(hand, "is replaced by a score of", sum_score)
    else:
        for n in range(len((hand))):
            hand_count.append(hand.count(hand[n]))
        sum_score = sum(hand_count)
            #print(hand[n], "komt", hand.count(hand[n]), "keer voor")
    if sum_score == 5:
        result = 1 # "High card"
    elif sum_score == 7:
        result = 2 #"One pair"  
    elif sum_score == 9:
        result = 3 #"Two pair"    
    elif sum_score == 11:
        result = 4 #"Three of a kind"   
    elif sum_score == 13:
        result = 5 #"Full house"                
    elif sum_score == 17:
        result = 6 #"Four of a kind"
    elif sum_score == 25:
        result = 7 # "Five of a kind"
    # print("this is hand:", hand, "with a result of:", result)
    hand_order.append([result, hand, bid])

# Check with hand in a specific hand score is higher
new_hand_order = []
for n in range(1,8):# numbers 1 t/m 7
    # print(n)
    temp_hands = []
    for hand in hand_order: 
        if hand[0] == n:
            temp_hands.append(hand)
    if temp_hands != []:
        #print(temp_hands)
        n = len(temp_hands)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                # print(temp_hands[j][1], temp_hands[j + 1][1])
                for l in range(len(temp_hands[j][1])):
                    # print(temp_hands[j][1][l], temp_hands[j + 1][1][l])
                    if replace_letter_2(temp_hands[j][1][l]) > replace_letter_2(temp_hands[j + 1][1][l]):
                        temp_hands[j], temp_hands[j + 1] = temp_hands[j + 1], temp_hands[j]
                        break
                    elif replace_letter_2(temp_hands[j][1][l]) < replace_letter_2(temp_hands[j + 1][1][l]):
                        break
        new_hand_order += temp_hands   

    
# Calculate the total
total = 0
for n in range(len(new_hand_order)):
    # print(new_hand_order[n][1])
    # print(int(new_hand_order[n][2]), (n+1))
    # print(int(new_hand_order[n][2]) * (len(new_hand_order) - n))
    total = total + (int(new_hand_order[n][2]) * (n+1))

print("The solution for part two is:", total)
# Fout: 254056319 (too low), 254387867 (too low), 254399831 (too low)