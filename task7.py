"""
Write a Python function named build_price_map(names, prices) that takes two lists:

names — a list of product names (strings)
prices — a list of integers representing the price for each product
You may assume both lists have the same length and that each position in the lists corresponds to a product and its price.

The function should return a dictionary mapping each product name to its corresponding price.

For example:

build_price_map(["pen", "paper", "eraser"], [5, 12, 3])
should return:

{"pen": 5, "paper": 12, "eraser": 3}

The function must not print anything; it should return the dictionary.

Note(s):

It is very important to return the dictionary exactly as specified.
The example inputs will be provided by the system during testing.
Assume both lists are valid and have equal length.
You have to click the check button for any attempt at an answer to be valid.


"""

def build_price_map(names, prices):
    result = dict(zip(names, prices))
    # print(result)
    return result

"""
# OR 

def build_price_map(names, prices):
    dict = {}
    index = 0
    while index < len(names):
        dict[names[index]] = prices[index]
        index += 1 
    print(dict)
"""
"""
# OR 

def build_price_map(names, prices):
    dict = {}
    
    for i in range(len(names)):
        dict[names[i]] = prices[i]
    print(dict)
"""

build_price_map(["pen", "paper", "eraser"], [5, 12, 3])