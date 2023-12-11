''' 
Advent of Code 2023
Day 10: Pipe Maze
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
        char_list = []
        for char in line:
            if char != ' ':
                char_list.append(char)
        new_content.append(char_list)
    return new_content

def fill_graph(list):
    graph = []
    id = 0
    for line in list:
        length = len(line)
        for char in line:
            start = False
            match char:
                case "S":
                    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
                    # S will have exactly two pipes connecting to it, and is assumed to connect back to those two pipes
                    start = True
                    connections = []
                case "|":
                    # | is a vertical pipe connecting north and south.
                    connections = [
                        (id - length) if (id - length) >= 0 else None, # "north" 
                        (id + length) if (id + length) >= 0 else None # "south"
                    ]
                case "-":
                    # - is a horizontal pipe connecting east and west.
                    connections = [
                        (id + 1) if (id + 1) >= 0 else None, # "east"
                        (id - 1) if (id - 1) >= 0 else None # "west"  
                    ]
                case "L":
                    # L is a 90-degree bend connecting north and east.
                    connections = [
                        (id - length) if (id - length) >= 0 else None, # "north" 
                        (id + 1) if (id + 1) >= 0 else None # "east"
                    ]
                case "J":
                    # J is a 90-degree bend connecting north and west.
                    connections = [
                        (id - length) if (id - length) >= 0 else None, # "north" 
                        (id - 1) if (id - 1) >= 0 else None # "west"  
                    ]
                case "7":
                    # 7 is a 90-degree bend connecting south and west.
                    connections = [
                        (id + length) if (id + length) >= 0 else None, # "south"
                        (id - 1) if (id - 1) >= 0 else None # "west"  
                    ]
                case "F":
                    # F is a 90-degree bend connecting south and east.
                    connections = [
                        (id + length) if (id + length) >= 0 else None, # "south"
                        (id + 1) if (id + 1) >= 0 else None # "east"
                    ]
                case other:
                    # . is ground; there is no pipe in this tile.
                    connections = []
            node = {
                "id": id,
                "character": char,
                "start": start,
                "connections": connections
            }
            graph.append(node)
            id += 1
    return graph

def define_start(graph, length):
    # find start
    start = next(item for item in graph if item["start"])
    start_id = start['id']
    # bekijk positie er omheen welke connect 
    north = next(item for item in graph if item["id"] == start_id - length)
    south = next(item for item in graph if item["id"] == start_id + length)
    east = next(item for item in graph if item["id"] == (start_id + 1))
    west = next(item for item in graph if item["id"] == (start_id - 1))
    if start_id in north["connections"]:
        start["connections"].append(north["id"])
    if start_id in south["connections"]:
        start["connections"].append(south["id"])
    if start_id in east["connections"]:
        start["connections"].append(east["id"])
    if start_id in west["connections"]:
        start["connections"].append(west["id"])
    return graph

def walk_arround(graph):
    # find start
    start = next(item for item in graph if item["start"])
    previous = start["id"]
    position = start["connections"][0]
    # Start walking
    steps = 1
    while True:
        #print(graph[position])
        if position == start["id"]:
            break
        current_connections = graph[position]["connections"]
        if current_connections[0] != previous:
            previous = position
            position = current_connections[0]
        else:
            previous = position
            position = current_connections[1]
        steps += 1
    return steps

# Part 1: Farthest position of the loop
content = single_char_list(read_file('test3.txt'))
content_graph = fill_graph(content)
define_start(content_graph, len(content[0]))
farthest_position = (walk_arround(content_graph)/2)
print("The solution for part one is:", int(farthest_position))

# Part 2:
# test 3 = 4, test4 = 8, test5 = 10

count = 0

print(0 % 2)
print(1 % 2)
print(2 % 2)
print(3 % 2)

for line in content:
    print(line)
    previous = "."
    current = "."
    inside = False
    cross = 0
    for next in line:
        cross = 0   
        if cross % 2 == 0: 
            if current != "."  and next == ".":
                inside = True
                count += 1
                cross += 1
            elif inside and current == "." and next == ".":
                inside = True
                count += 1
            elif current == "." and next != ".":
                inside = False
            
        else:
            inside = False
        print(previous, current, next, inside, "cross:", cross)
        
        
        # if next != current:
        #     print(previous, current, next)
        #     if previous != "." and current == "." and next != ".":
        #         print("binnenkand?")
        previous = current
        current = next
    print(count)


