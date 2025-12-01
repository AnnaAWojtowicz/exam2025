# syntax for csv files:

# newline=""    <- This prevents Python from inserting extra blank lines in the CSV file


import csv

# HOW TO OPEN A FILE:

with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file) # <- prints in form of dictionary {}
        #reader = csv.reader(file) # <- prints in form of list []
        next(reader) # <- skips the header
        for row in reader:
                # sth sth sth
                row = row.strip() # <- .strip() removes whitespace, such as: spaces " ", tabs \t, newlines \n





# HOW TO SAVE A FILE:

with open(filename, "w", newline="") as file:

    # writer = csv.writer(file)     <- if you use this, row must be a list or tuple. (rows1)
    fieldnames = ["name", "age", "city"]    # <- check the next line!
    writer = csv.DictwWriter(file, fieldnames=fieldnames)  # <- this lets write rows as dictionaries where keys = fieldnames (rows2)
    
    writer.writeheader()    # <- This writes header with fieldnames
    writer.writerows(rows)  # <- This writes multiple rows to the CSV file at once.
    # writer.writerows(row)     <- This writes one row to the CSV file.

# examples of rows: 
    rows1 = [
    ["Anna", 29],
    ["Mark", 33],
    ["John", 25]
]
    
    # result for rows1:

    # Anna,29
    # Mark,33
    # John,25


    rows2 = [
    {"name": "Anna", "age": 29, "city": "Oslo"},
    {"name": "Mark", "age": 33, "city": "London"},
]
    
    # result of rows2:

    # name,age,city
    # Anna,29,Oslo
    # Mark,33,London 
