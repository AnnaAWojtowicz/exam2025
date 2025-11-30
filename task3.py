"""
Write a Python function named count_below_50(values) that takes a list of integers called values as a parameter.

The function should return the number of elements in the list that are strictly less than 50.

For example:

count_below_50([10, 60, 49, 50, 80])
should return 2 (only 10 and 49 are less than 50).

Another example:

count_below_50([100, 51, 50])
should return 0.

Note(s):

It is very important to match the output shown in the examples precisely. Return values must be exactly as specified.
The example inputs, as shown above, will be provided by the system when testing. You should only write the function you are asked to write.
Assume all input lists are valid and contain only integers.
You have to click the check button for any attempt at an answer to be valid.
For example:

Test	Result
print(count_below_50([10, 60, 49, 50, 80]))
2
"""


def count_below_50(values):
    container = []
    for value in values:
        if value < 50:
            container.append(value)
    result = len(container)
    print(result)
    return result

count_below_50([10, 60, 20, 50, 10])