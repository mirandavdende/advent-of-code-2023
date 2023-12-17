''' 
Advent of Code 2023
Day 15: Lens Library
'''
def read_file(file):
    ''' Open file, read content and remove new lines'''
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def calculate_HASH(input):
    result = 0
    for i in input:
        # Determine the ASCII code for the current character of the string. --> ord(value)
        # Increase the current value by the ASCII code you just determined.
        result = result + ord(i)
        # Set the current value to itself multiplied by 17.
        result = result * 17
        # Set the current value to the remainder of dividing itself by 256.
        result = result % 256
    return result

def calculate_total(input):
    total = 0
    input = input.split(',')
    for block in input:
        result = calculate_HASH(block)
        total = result + total
    return total

def boxes_list(ammount):
    boxes = []
    for n in range(ammount):
        box = {
            "box": n,
            "lenses": [],
        }
        boxes.append(box)
    return boxes

def boxes(input):
    input = input.split(',')
    boxes = boxes_list(256) 
    for block in input:
        if "=" in block:
            operator = "="
            block_split = block.split("=")
            label = block_split[0]
            focal_length = block_split[1]
            box_nr = calculate_HASH(label)
            boxes = operation_equals(operator, label, box_nr, boxes, focal_length)
        elif "-" in block:
            operator = "-"
            label = block.split("-")[0]
            box_nr = calculate_HASH(label)
            boxes = operation_dash(operator, label, box_nr, boxes)    
    return boxes

def operation_dash(operator, label, box_nr, boxes):
    # dash (-): go to the relevant box and remove the lens with the given label if it is present in the box. 
    # Move any remaining lenses as far forward in the box as they can go without changing their order.
    for box in boxes:
        if box["box"] == int(box_nr):
            if [i for i in box["lenses"] if label in i]:
                remove = [i for i in box["lenses"] if label in i]
                for n in range(len(remove)):
                    remove_label = remove[n].split(" ")
                    if remove_label[0] == label:
                        box["lenses"].remove(remove[n])    
    return boxes

def operation_equals(operator, label, box_nr, boxes, focal_length):
    for box in boxes:
        if box["box"] == int(box_nr):
            # equals sign (=): inumber indicating the focal length of the lens that needs to go into the relevant box; 
            if box["lenses"] == []: # no lenses in box
                box["lenses"] = [str(label + " " + focal_length)]
            elif [i for i in box["lenses"] if label in i]:
                # Already a lens in the box with the same label, replace the old lens with the new lens: 
                # remove the old lens and put the new lens in its place, not moving any other lenses in the box.
                replace = [i for i in box["lenses"] if label in i]
                for n in range(len(replace)):
                    replace_label = replace[n].split(" ")
                    if replace_label[0] == label:   
                        index = box["lenses"].index(replace[n]) 
                        box["lenses"][index] = str(label + " " + focal_length)
            else:
                # If there is not already a lens in the box with the same label, add the lens to the box immediately behind any lenses already in the box.
                box["lenses"].append(str(label + " " + focal_length))
    return boxes

def focusing_power(input):
    total = 0
    for box in input:
        box_nr = box["box"]
        lenses = box["lenses"]
        slot = 1
        if box["lenses"] != []:
            for lens in lenses:
                focal_length = str(0)
                for i in lens:
                    if i.isdigit():
                        focal_length = focal_length + i
                focusing_lens = (1+box_nr) * slot * int(focal_length)
                slot += 1
                total = total + focusing_lens
    return total

# Part 1: read the HASH
content = read_file('input.txt')
print("The solution for part one is:", calculate_total(content[0])) # 517551

# Part 2: HASHMAP
boxes = boxes(content[0])
print("The solution for part one is:", focusing_power(boxes)) # 286097
