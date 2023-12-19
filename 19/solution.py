''' 
Advent of Code 2023
Day 19: Aplenty
'''
import re

def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def rules_parts(input):
    rules = []
    parts = []
    for line in input:
        if len(line) == 0:
            pass
        elif line[0] == "{":
            parts.append(line)
        else:
            rules.append(line)
    return rules, parts

def extract_values(part):
    part = part.split(",")
    for category in part:
        if "x" in category:
            x = ""
            for l in category:
                if l.isdigit():
                    x += l 
        elif "m" in category:
            m = ""
            for l in category:
                if l.isdigit():
                    m += l 
        elif "a" in category:
            a = ""
            for l in category:
                if l.isdigit():
                    a += l 
        elif "s" in category:
            s = ""
            for l in category:
                if l.isdigit():
                    s += l 
    return int(x), int(m), int(a), int(s)

def extract_rules(rules):
    rules_dict = {}
    for rule in rules:
        rule = rule.split("{")
        name = rule[0]
        rule[1] = rule[1][:-1]
        index_larger, index_smaller = [], []
        if "<" in rule[1]:
            index_smaller = [i for i, n in enumerate(rule[1]) if n == "<"] 
        if ">" in rule[1]:
            index_larger = [i for i, n in enumerate(rule[1]) if n == ">"] 
        index_list = sorted(index_larger + index_smaller)
        
        rule_list = []
        n_1 = 0
        if len(index_list) > 1:
            for n in range(len(index_list)-1):
                new_rule = rule[1][n_1:(index_list[n+1]-1)].replace(',', '') 
                rule_list.append(new_rule)
                n_1 = index_list[n+1]-1
            rule_list.append(rule[1][(index_list[n+1]-1):])
        else:
            rule_list.append(rule[1])

        keys_dict = {}
        count = 0
        for rule in rule_list:
            catogory = rule[0]
            sign = rule[1]
            rule = rule.split(":")
            value = int(rule[0][2:])
            go_to = rule[1].split(",")
            go_to_true = go_to[0]
            if len(go_to) > 1:
                go_to_false = go_to[1]
            else:
                go_to_false = None
            cat_dict = {
            "catogory": catogory,
            "sign": sign,
            "value": value,
            "go_to_true": go_to_true,
            "go_to_false": go_to_false
            }       
            keys_dict["key_"+str(count)] = cat_dict
            count += 1
        rules_dict[name] = keys_dict
    return rules_dict

def apply_rules(rules_dict, parts):
    total = 0
    for part in parts:
        x, m, a, s = extract_values(part)
        rule_key = "in"
        A = False
        R = False

        while not A and not R:
            rule = rules_dict[rule_key]
            for key in rule.keys():
                catogory = rule[key]["catogory"]
                sign = rule[key]["sign"]
                value = rule[key]["value"]
                match catogory:
                    case "x":
                        if sign == "<":
                            if x < value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                        else:
                            if x > value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                    case "m":
                        if sign == "<":
                            if m < value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                        else:
                            if m > value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                    case "a":
                        if sign == "<":
                            if a < value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                        else:
                            if a > value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                    case "s":
                        if sign == "<":
                            if s < value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                        else:
                            if s > value:
                                rule_key = rule[key]["go_to_true"]
                            else:
                                rule_key = rule[key]["go_to_false"]
                if rule_key == None:
                    pass
                else:
                    break
            if rule_key == "A":
                A = True
            elif rule_key == "R":
                R = True
        
        if A:
            accepted = x + m + a + s
            total += accepted
    return total

# Part 1: sort the parts
content = read_file('input.txt')
rules, parts = rules_parts(content)
rules_dict = extract_rules(rules)
total = apply_rules(rules_dict, parts)
print("The solution for part one is:", total) #373302

# Part 2: 


