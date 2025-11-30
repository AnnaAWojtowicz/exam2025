"""
Write a Python procedure named print_negative(values) that takes a list of integers called values as a parameter.

The procedure should print each negative number from the list on its own line, in the order they appear.

For example, calling the procedure as shown below:

print_negative([-5, 3, -2, 7])
should produce the output:

-5
-2
The procedure must not return any value.

Note(s):

It is very important to match the output shown in the example(s) precisely (case-sensitive and line breaks must match).
The example inputs, as shown above, will be provided by the system. You should only write the procedure you are asked to write.
Assume all input lists are valid and contain only integers.
You have to click the check button for any attempt at an answer to be valid.
For example:

Test	Result
print_negative([-5, 3, -2, 7])
-5
-2
"""


def print_negative(values):
    for value in values:
        if value < 0:
            print(value)

print_negative([-5, 3, -2, 7])