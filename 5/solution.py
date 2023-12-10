''' 
Advent of Code 2023
Day 5: If You Give A Seed A Fertilizer
'''
# Open file and read content
f = open('test.txt', 'r')
lines = f.readlines()
f.close()

# remove new lines
content = []
for l in lines:
    if l != '\n':
        content.append(l.replace("\n", " "))

# Part 1: find the lowest location number that corresponds to any of the initial seeds
# Numbers corospond to destination range start, the source range start, and the range length
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

# Make a list of seed numbers that we need to look up
seeds = content[0].split()
del seeds[0]
for i in range(0, len(seeds)):
    seeds[i] = int(seeds[i])

# Make a dataframe with all the map numbers
del content[0]
map_dict = {}
for line in content:
    if not line[0].isdigit():
        key = line 
        map_dict[key] = []
    else:
        numbers = line.split(" ")
        while("" in numbers):
            numbers.remove("")
        map_dict[key].append(numbers)

map_dict[0] = map_dict.pop("seed-to-soil map: ")
map_dict[1] = map_dict.pop("soil-to-fertilizer map: ")
map_dict[2] = map_dict.pop("fertilizer-to-water map: ")
map_dict[3] = map_dict.pop("water-to-light map: ")
map_dict[4] = map_dict.pop("light-to-temperature map: ")
map_dict[5] = map_dict.pop("temperature-to-humidity map: ")
map_dict[6] = map_dict.pop("humidity-to-location map: ")

# Make a dataframe to store the numbers for each seed
import pandas as pd
data = {
  "seed": seeds,
  "soil": seeds,
  "fertilizer": seeds,
  "water": seeds,
  "light": seeds,
  "temperature": seeds,
  "humidity": seeds,
  "location": seeds
}
df = pd.DataFrame(data)

for col in range(len(df.columns)-1):
    # print("col n:", col)
    map = map_dict[col]
    for row in range(len(df.index)):
        #print("row n:", row, "value:", df.iloc[row,col] )
        number = df.iloc[row,col]
        df.iloc[row,col+1] = df.iloc[row,col]
        for map_row in map:
            #print(map_row)
            des_start, source_start, range_length = map_row
            if int(source_start) <= number <= (int(source_start) + int(range_length)):
                difference = number - int(source_start)
                new_number = int(des_start) + difference
            # des_start_list = []
            # source_start_list = []
            # for n in range(int(range_length)):
            #     des_start_list.append((int(des_start) + n))
            #     source_start_list.append((int(source_start) + n))
            # print("des_start_list", des_start_list)
            # print("source_start_list", source_start_list)
            # if int(df.iloc[row,col]) in source_start_list:
                # index = source_start_list.index(df.iloc[row,col])
                df.iloc[row,col+1] = new_number
                #print(df.iloc[row,col], "is in range and will be replaced by", des_start_list[index])
                break

print("The solution for part one is:", df['location'].min())

# part 2:
def overlap(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )


# df_2 = pd.DataFrame(columns=['seed','soil','fertilizer','water','light','temperature','humidity'])
df_2 = pd.DataFrame()
sublists_seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

for col in map_dict:
    print("col n:", col)
    new_seeds = [] # BUG?: new_seeds wordt gereset voor elke gang door alle mappings, maar elke mapping voegt elke seed toe
    # print("col n:", col, "The seeds are", sublists_seeds)
    for map in map_dict[col]:
        # print(map) 
        des_start = int(map[0])
        source_start = int(map[1])
        range = int(map[2])
        source_end = int(map[1]) + int(map[2]) - 1
        print(f"Evaluating mapping [{source_start} - {source_end}]")
        
        for n in sublists_seeds:
            seed_start = n[0]
            seed_range_length = n[1]
            seed_end = seed_start + seed_range_length - 1
            print(f"* Seed [{seed_start} - {seed_end}]")
            if seed_start >= source_start and seed_end <= source_end: # 79 >= 50 92 <= 97
                print("  -> Helemaal in range")
                new_seed_start = seed_start # BUG: was des_start
                new_seed_range_length = seed_range_length
                new_seeds.append([new_seed_start, new_seed_range_length])
                # list met nieuwe seeds
            elif seed_start <= source_start <= seed_end: # 55 <= 64 <= 67 --> Begin source ligt er in
                print("  -> Begin in range")
                # range 1: seed_start tot source_start --> blijft hetzelfde
                new_seed_start_1 = seed_start
                new_seed_range_length_1 = source_end - seed_start + 1
                new_seeds.append([new_seed_start_1, new_seed_range_length_1])
                # range 2: source_start tot seed_end --> des_start
                new_seed_start_2 = des_start
                new_seed_range_length_2 = seed_range_length - new_seed_range_length_1
                new_seeds.append([new_seed_start_2, new_seed_range_length_2])
            elif seed_start <= source_end <= seed_end: # 55 <= 60 <= 67 --> source Eind ligt er in
                print("  -> Eind in range")
                # range 1: seed_start tot source_end --> word anders
                new_seed_start_1 = des_start
                new_seed_range_length_1 = source_end - seed_start +1
                new_seeds.append([new_seed_start_1, new_seed_range_length_1])                
                # range 2: source_end tot seed_end --> blijft hetzelfde
                new_seed_start_2 = source_end
                new_seed_range_length_2 = seed_range_length - new_seed_range_length_1
                new_seeds.append([new_seed_start_2, new_seed_range_length_2])
            else:
                print(f"  -> Niet in de range")
                new_seeds.append([seed_start, seed_range_length])
    sublists_seeds = new_seeds
    print(new_seeds)
    break



# 15 - 19 blijft dan gewoon 15 - 19, want geen mapping
# 20 - 24 word dan 30 - 34, want wel een mapping

# Eindresultaat: 15 - 19 en 30 - 34. Laagste waarde: 15.

# Je hoeft dus op deze manier alle tussenliggende waarden niet uit te rekenen, wat super veel scheelt.
                    



# count = 0
# seed_list = []
# for col in map_dict:
    
#     print(seeds[count])
#     temp_list = []
#     for map in map_dict[col]:
#         print(map)
#         des_start = int(map[0])
#         source_start = int(map[1])
#         range = int(map[2])
#         source_end = int(map[1]) + int(map[2])


        
#         n = 0
#         print(len(seeds[count]))

#         for x in range((len(seeds[count])/2)): 
#             seed_start = int(seeds[count][x+n])
#             print("seed_start", seed_start)
#             seed_range_length = int(seeds[count][x+n+1])
#             print("seed_range_length", seeds[count][x+n+1])
#             seed_end = seed_start + seed_range_length
            
#             n += 1
            
#             # find = overlap(source_start, source_end, seed_start, seed_end)
            
#             # if find == True:
#             if source_start < seed_start and seed_end < source_end: # Helemaal er in
#                 print("Helemaal in range")
#                     # temp_list.append(des_start + (seed_start-source_start))
#                     # temp_list.append(seed_range_length)
#             elif source_start > seed_start and seed_end < source_end: # Begin er niet in, einde wel
#                 print("Begin in range")
#                     # seed_start_1 = seed_start
#                     # seed_range_length_1 = source_start - seed_start
#                     # seed_start_2 = source_start
#                     # seed_range_length_2 = seed_range_length - seed_range_length_1
#                     # temp_list.append(seed_start_1)
#                     # temp_list.append(seed_range_length_1)
#                     # temp_list.append(seed_start_2)
#                     # temp_list.append(seed_range_length_2)
#             elif source_start > seed_start and seed_end > source_end:
#                 print("Eind in range")
#                     # seed_start_1 = source_start
#                     # seed_range_length_1 = source_start + source_start_range
#                     # seed_start_2 = source_start + source_start_range
#                     # seed_range_length_2 = seed_range_length - seed_range_length_1
#                     # temp_list.append(seed_start_1)
#                     # temp_list.append(seed_range_length_1)
#                     # temp_list.append(seed_start_2)
#                     # temp_list.append(seed_range_length_2)
#             else:
#                 print("Niet in range")
#                 # temp_list.append(seed_start)
#                 # temp_list.append(seed_range_length)
#             #print("New seeds list:", temp_list)
#         seeds.append(temp_list)
#         count += 1

# #print(seeds)

# # Stel je hebt input `15 10` (dus waarden 15 t/m 24)
# # En dan heb je mapping `30 20 10` (dus waarden van 20 - 29 gaan naar 30 - 39)
# # Je hoeft eigenlijk alleen maar naar de randwaarden van de input en de mappings te kijken, niet naar alles er tussen in. En omdat 20 (de randwaarde van de mapping) tussen 15 en 14 ligt moet je dan die input opsplitsen. Dus:
# # 15 - 24 => 15 - 19, 20 - 24

# # 15 - 19 blijft dan gewoon 15 - 19, want geen mapping
# # 20 - 24 word dan 30 - 34, want wel een mapping

# # Eindresultaat: 15 - 19 en 30 - 34. Laagste waarde: 15.

# # Je hoeft dus op deze manier alle tussenliggende waarden niet uit te rekenen, wat super veel scheelt.
                    

#                 # difference = number - int(source_start)
#                 # new_number = int(des_start) + difference
#                 # df.iloc[row,col+1] = new_number
#                 #print(df_2.iloc[row,col], "is in range and will be replaced by", des_start_list[index])
#                 # break            


# #print("The solution for part two is:", df_2['location'].min())