"""
Write a Python function named shortest_word(words) that takes a list of strings called words and returns the shortest word in the list.

If multiple words have the same shortest length, the function should return the first such word.

You may NOT use any of the following Python features:

min()
sorted()
len() on the list itself (using len(word) on individual items is allowed)
List comprehensions
Slicing (e.g. words[1:])
You must determine the shortest word using manual iteration and comparison.

For example:

shortest_word(["elephant", "cat", "zebra"])  →  "cat"
Another example:

shortest_word(["hi", "to", "at"])  →  "hi"
The function must return the result, not print it.

Note(s):

It is very important that your function adheres to the above restrictions.
The example inputs will be provided by the system during testing.
Assume the list contains at least one valid string.
You have to click the check button for any attempt at an answer to be valid.
"""


def shortest_word(words):
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    #print(shortest)
    return shortest


shortest_word(["elephant", "cat", "zebra"]) 
shortest_word(["hi", "to", "at"]) 