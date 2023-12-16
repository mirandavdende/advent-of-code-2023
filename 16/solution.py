''' 
Advent of Code 2023
Day 16: The Floor Will Be Lava
'''

def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def beam_locations_list(start, input):
    # Start coordinate
    beam_locations = start

    while any(beam["running"] for beam in beam_locations):
        for beam in beam_locations:
            if beam["running"]:
                if beam["split"]: # duplicate and change direction
                    new_beam_1, new_beam_2 = split(beam, input)
                    beam["running"] = False
                    #print("Old:", beam)
                    #print("New:", new_beam_1, new_beam_2 )
                    # kijk of de locatie al geweest is in deze richting
                    present = find_beam(beam_locations, new_beam_1)
                    if not present and new_beam_1["running"]:
                        beam_locations.append(new_beam_1)
                    present = find_beam(beam_locations, new_beam_2)
                    if not present and new_beam_2["running"]:
                        beam_locations.append(new_beam_2)
                else:
                    new_beam = next_location(beam, input)
                    beam["running"] = False
                    #print("Old:", beam)
                    #print("New:", new_beam)
                    present = find_beam(beam_locations, new_beam)
                    if not present and new_beam["running"]:
                        beam_locations.append(new_beam)
    return beam_locations

def find_beam(haystack, needle):
    for n in haystack:
        if n["x"] == needle["x"] and n["y"] == needle["y"] and n["direction"] == needle["direction"]:
            return n
    return None

def next_location(beam, input):
    x_cor = beam["x"]
    y_cor = beam["y"]
    direction = beam["direction"]
    x_len = len(input[0])
    y_len = len(input)

    match direction:
        case "right":
            x_cor += 1
        case "left":
            x_cor -= 1
        case "up":
            y_cor -= 1
        case "down":
            y_cor += 1
    
    # index out of range = niet meer running 
    if x_cor > x_len-1 or y_cor > y_len-1 or x_cor < 0 or y_cor < 0:
        return {
            "x": x_cor,
            "y": y_cor,
            "direction": direction,
            "running": False,
            "split": split
        }

    # Check wat we tegenkomen op het speelveld
    match input[y_cor][x_cor]:
        case '.':
            return {
                "x": x_cor,
                "y": y_cor,
                "direction": direction,
                "running": True,
                "split": False
            }

        case '|':
            return {
                "x": x_cor,
                "y": y_cor,
                "direction": direction,
                "running": True,
                "split": direction == "right" or direction == "left"
            }

        case '-':
            return {
                "x": x_cor,
                "y": y_cor,
                "direction": direction,
                "running": True,
                "split": direction == "up" or direction == "down"
            }

        case '/':
            match direction:
                case "right":
                    direction = "up"
                case "left":
                    direction = "down"
                case "up":
                    direction = "right"
                case "down":
                    direction = "left"

        case '\\':
            match direction:
                case "right":
                    direction = "down"
                case "left":
                    direction = "up"
                case "up":
                    direction = "left"
                case "down":
                    direction = "right"

    # Return voor de laatste twee cases
    return {
        "x": x_cor,
        "y": y_cor,
        "direction": direction,
        "running": True,
        "split": False
    }

def split(beam, input):
    # wissel van direction als split true is en split de beam 
    x_cor = beam["x"]
    y_cor = beam["y"]
    location = input[y_cor][x_cor]
    direction = beam["direction"]

    match location:
        case "|":
            # print("split |", y_cor, x_cor)
            direction_1 = "up"
            direction_2 = "down"
        case "-":
            # print("split -", y_cor, x_cor)
            direction_1 = "left"
            direction_2 = "right"
    new_beam_1 = {
        "x": x_cor,
        "y": y_cor,
        "direction": direction_1,
        "running": True,
        "split": False
    }
    new_beam_2 = {
        "x": x_cor,
        "y": y_cor,
        "direction": direction_2,
        "running": True,
        "split": False
    }
    return new_beam_1, new_beam_2 

def count_energized(places, content):
    total = 0
    count = 0
    for y in range(len(content)):
        # print(count, ":", end='')
        for x in range(len(content[0])):
            present = next((item for item in places if item["x"] == x and item["y"] == y), None)
            if present:
                # print("#", end='')
                total+=1
            # else:
                # print(".", end='')
        # print()
        count += 1
    return total

def generate_start_locations(input):
    start_list = []
    x_len = len(input[0])
    y_len = len(input)
    
    y_cor = -1
    for x in range(x_len):
        x_cor = x
        start = [{
            "x": x_cor,
            "y": y_cor,
            "direction": "down",
            "running": True,
            "split": False
        }]
        start_list.append(start)
    
    y_cor = y_len + 1
    for x in range(x_len):
        x_cor = x
        start = [{
            "x": x_cor,
            "y": y_cor,
            "direction": "up",
            "running": True,
            "split": False
        }]
        start_list.append(start)
    
    x_cor = -1
    for y in range(y_len):
        y_cor = y 
        start = [{
            "x": x_cor,
            "y": y_cor,
            "direction": "right",
            "running": True,
            "split": False
        }]
        start_list.append(start)
    
    x_cor = x_len + 1
    for y in range(y_len):
        y_cor = y 
        start = [{
            "x": x_cor,
            "y": y_cor,
            "direction": "left",
            "running": True,
            "split": False
        }]
        start_list.append(start)

    return start_list

def most_energized(start_list, input):
    higest_count = 0
    for start_location in start_list:
        places = beam_locations_list(start_location, input)
        count = count_energized(places, input)
        if count > higest_count:
            higest_count = count
    return higest_count

# Part 1: which tiles become energized
content = read_file('input.txt')
start = [{
    "x": -1,
    "y": 0,
    "direction": "right",
    "running": True,
    "split": False
}]
places = beam_locations_list(start, content)
print("The solution for part one is:", count_energized(places, content)) # 6622

# Part 2: Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
start_list = generate_start_locations(content)
print("The solution for part two is:", most_energized(start_list, content)) # 7130


