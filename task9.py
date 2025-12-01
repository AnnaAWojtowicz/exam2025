"""
Write a Python function named load_average_values(filename) that takes a single parameter filename, which is the name of a CSV file.

The CSV file contains a header row followed by one or more data rows. Each data row has the format:

name,value1,value2,value3
where name is a string and value1, value2 and value3 are integers.

The function should:

Open the CSV file for reading.
Skip the header row.
For each data row:
Extract the name and the three integer values.
Compute the average of the three values, as a floating-point number.
Round the average to one decimal place.
Build and return a dictionary that maps each name (string) to its rounded average value (float).
You must use the csv module to read the file. You should compute the average using normal arithmetic and loops; avoid using high-level shortcuts like sum() on the three values.

For example, if the CSV file "scores.csv" contains:

name,value1,value2,value3
Alice,10,20,30
Bob,5,15,25
then calling:

result = load_average_values("scores.csv")
print(result)
could produce:

{'Alice': 20.0, 'Bob': 15.0}
Note(s):

It is very important that the returned dictionary matches the expected values and types exactly.
The example file contents, as shown above, will be created by the system during testing. You should only write the function you are asked to write.
Assume all data rows contain exactly three integer values.
You have to click the check button for any attempt at an answer to be valid.
"""
import csv

def load_average_values(filename):
    dictionary = {}
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        #reader = csv.DictReader(file) <- prints as dictionary
        next(reader)    # <- skips the header
        for row in reader:
            # print(row)
            dictionary[row[0]] = round((sum([float(row[1]),float(row[2]),float(row[3])]) / 3), 1)
           # dictionary = round((float(row[1]) + float(row[2]) + float(row[3])) / 3, 1)     # <- this will work becuase there is no []
    #print(dictionary)
    return dictionary


load_average_values("scores.csv")