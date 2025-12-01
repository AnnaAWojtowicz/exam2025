"""
# task1
user_input = int(input("Enter temperature in Celsius: "))
def temp(user_input):
    if user_input < 10:
        print("Cold")
    elif 10 <= user_input <= 24:
        print("Warm")
    else:
        print("Hot")

temp(user_input)
"""

"""
# task2

total_count = 0

def divide(num):
    count = 0
    if num % 5 == 0:
        count += 1
    return count

keep_going = True

while keep_going:

    user_input = int(input("Enter a positive integer (0 to stop): "))
    
    if user_input == 0:
        keep_going = False
        break
    elif user_input < 0:
        print("You have to enter a positive integer. Try again")
    
    total_count += divide(user_input)

print(total_count)
"""

"""
# task 3

def count_below_50(values):
    count = 0
    for value in values:
        if value < 50:
            count += 1
    return count

print(count_below_50([10, 60, 49, 50, 80]))
"""

"""
# task 4

def print_negative(values):
    for value in values:
        if value < 0:          
            print(value)

print_negative([-5, 3, -2, 7])
"""

"""
# task 5

def count_starting_with(words, letter):
    count = 0
    for word in words:
        if word[0] == letter:
            count += 1
    print(count)
    return count

count_starting_with(["dog", "door", "cat"], "d")
count_starting_with(["Apple", "ant", "anchor", "Allah", "asterix"], "a")
"""

"""
# task 6

def shortest_word(words):
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    #print(shortest)
    return shortest

shortest_word(["elephant", "cat", "zebra"]) 
"""

"""

# task7

def build_price_map(names, prices):
    dict = {}
    index = 0
    while index < len(names):
        dict[names[index]] = prices[index]
        index += 1 
    print(dict)

build_price_map(["pen", "paper", "eraser"], [5, 12, 3])
"""

"""
# task 8

def find_top_total_from_file(filename):
    dict = {}
    with open(filename, "r") as file:
        for row in file:
            row = row.strip()
            if row == "":
                continue
            name, value = row.split()
            if name in dict: 
                dict[name] += int(value)
            else:
                dict[name] = int(value)
        name = max(dict, key=dict.get)
        highest_value = max(dict.values())
        highest = (name, highest_value)
    #print(highest)
    return highest

find_top_total_from_file("data.txt")
"""

"""
# task9
import csv

def load_average_values(filename):
    dict = {}
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            # dict[row[0]] = round((sum([float(row[1]),float(row[2]),float(row[3])]) / 3), 1)
            dict[row[0]] = round((float(row[1]) + float(row[2]) + float(row[3])) / 3, 1)
    #print(dict)
    return dict

load_average_values("scores.csv")

"""