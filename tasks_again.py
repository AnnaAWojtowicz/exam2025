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

"""
# task2



total_count = 0

def divide(num):
    count = 0
    if num % 5 == 0:
        count += 1
    return count

keep_going = True

while keep_going:

    user_input = int(input("Enter a positive integer (0 to stop): "))
    
    if user_input == 0:
        keep_going = False
        break
    elif user_input < 0:
        print("You have to enter a positive integer. Try again")
    
    total_count += divide(user_input)

print(total_count)

    
"""
    