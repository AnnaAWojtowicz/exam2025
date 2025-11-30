"""
Write a Python program that asks the user to enter an integer representing the temperature in Celsius.

The program should then:

Print Cold if the temperature is below 10.
Print Warm if the temperature is between 10 and 24 (inclusive).
Print Hot if the temperature is 25 or above.
The user must be prompted using the exact text:

Enter temperature in Celsius: 
For example, if the user enters 5, the output should be:

Enter temperature in Celsius: Cold
If the user enters 23, the output should be:

Enter temperature in Celsius: Warm
If the user enters 30, the output should be:

Enter temperature in Celsius: Hot
Note(s):

It is very important to match the text displayed to the user and the output shown precisely to the provided example(s). Output must match the text exactly (case-sensitive).
The example inputs, as shown above, will be provided by the system. You should only write the code you are asked to write.
Assume all input is valid unless otherwise stated.
You have to click the check button for any attempt at an answer to be valid.
For example:

Input	Result
5
Enter temperature in Celsius: 5
Cold

"""

user_input = int(input("Enter temperature in Celsius: "))

def temp(input):
    if input < 10:
        print("Cold")
    elif 10 <= input <= 24:
        print("Warm")
    else: 
        print("Hot")

temp(user_input)