"""
Write a Python program that repeatedly asks the user to enter a positive integer. The program must stop when the user enters 0.

The program should count how many of the entered values (excluding the final 0) were divisible by 5. After the user enters 0, the program should print the count.

The user must be prompted using the exact text:

Enter a positive integer (0 to stop): 
For example, if the user enters:

Enter a positive integer (0 to stop): 10 
Enter a positive integer (0 to stop): 8
Enter a positive integer (0 to stop): 25
Enter a positive integer (0 to stop): 0 
The output should be:2
Note(s):

It is very important to match the text displayed to the user and the output shown precisely to the provided example(s). Output must match the text exactly (case-sensitive).
The example inputs, as shown above, will be provided by the system. You should only write the code you are asked to write.
Assume all input is valid unless otherwise stated.
You have to click the check button for any attempt at an answer to be valid.

"""
count = 0
def divide(num):
    global count
    if num % 5 == 0:
        count += 1
    return count

keep_going = True

while keep_going:
    user_input = int(input("Enter a positive integer (0 to stop): "))
    
    if user_input == 0:
        keep_going = False
        break

    divide(user_input)
print(count)
