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

""""""
# task2

user_input = int(input("Enter a positive integer (0 to stop): "))


def divide(num):
    count = 0
    if num % 5 == 0:
        count += 1
    return count

keep_going = True
while keep_going:
    divide(user_input)

    

    