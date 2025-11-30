"""
Write a Python function named find_top_total_from_file(filename) that takes a single parameter filename, which is the name of a text file.

The text file contains zero or more non-empty lines. Each non-empty line contains a name and an integer value separated by a space, for example:

Alice 10
Bob 5
Alice 7
Charlie 3
The function should:

Open the file for reading.
Ignore any blank or whitespace-only lines.
For each non-empty line, split the line into a name (string) and a value (integer).
Accumulate the total value for each name in a dictionary.
Determine which name has the highest total value.
Return a tuple (name, total) where name is the name with the highest total and total is its total value as an integer.
If several names share the same highest total, you should return the first such name encountered when scanning through the dictionary.

For example, if the file contains:

Alice 10
Bob 5
Alice 7
Charlie 3
then calling:

result = find_top_total_from_file("data.txt")
print(result)
could produce:

('Alice', 17)
Note(s):

It is very important to match the format of the returned tuple exactly as shown in the example(s).
The example file contents, as shown above, will be created by the system during testing. You should only write the function you are asked to write.
Assume all non-empty lines in the file are valid and contain a name and an integer value separated by a space.
You have to click the check button for any attempt at an answer to be valid.

"""


def find_top_total_from_file(filename):
    dictionary = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, some_value = line.split()
            if name in dictionary:
                dictionary[name] += int(some_value)
            else: 
                dictionary[name] = int(some_value)
        highest_name = max(dictionary, key = dictionary.get)
        highest_value = max(dictionary.values())
        highest = (highest_name, highest_value)
            
        #print(highest)
        return highest


find_top_total_from_file("data.txt")
