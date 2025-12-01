# syntax for try-catch error thingy


try:
    #some code
    print("I'm awsome!")
except ValueError:
    print("That is not a valid number")
except ZeroDivisionError:
    print("You can't divide by 0")
except FileNotFoundError:
    print("There is no such file")
