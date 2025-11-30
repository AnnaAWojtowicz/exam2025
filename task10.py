"""
You must write several functions that work together to analyse product rating data stored in a CSV file.

The CSV file is always in the following format:

product,rating
Mouse,5
Keyboard,4
Mouse,3
Monitor,5
The file contains a header row followed by one or more data rows. Each data row contains a product name and an integer rating (for example, from 1 to 5).

You must define the following three functions:

load_ratings(filename)
Takes a single parameter filename (the name of the CSV file).
The function should:
Open the CSV file for reading.
Skip the header row.
Build and return a dictionary mapping each product name (string) to a list of its integer ratings.
Example return value:

{'Mouse': [5, 3], 'Keyboard': [4], 'Monitor': [5]}
average_ratings(ratings_dict)
Takes a dictionary of product ratings, as returned by load_ratings.
The function should:
Compute the average rating for each product.
Round each average to one decimal place.
Return a new dictionary mapping each product name to its average rating (float).
Example:

{'Mouse': [5, 3], 'Keyboard': [4], 'Monitor': [5]}
becomes:

{'Mouse': 4.0, 'Keyboard': 4.0, 'Monitor': 5.0}
print_rating_report(filename)
A procedure (no return value) that:
Calls load_ratings(filename) to read the data.
Calls average_ratings(...) to get the average rating per product.
Finds the product with the highest average rating.
Prints a single summary line in the format:
Top rated product: PRODUCT with average rating X.X
If several products share the same highest average rating, print the first encountered.

Note(s):

It is very important to match the text displayed to the user and the output shown precisely to the provided example(s). Output must match the text exactly (case-sensitive).
The example inputs, as shown below, will be provided by the system. You should only write the code you are asked to write.
Assume all input data is valid unless otherwise stated.
You have to click the check button for any attempt at an answer to be valid.
"""