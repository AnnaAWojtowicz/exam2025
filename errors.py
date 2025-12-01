# syntax for try-catch error thingy


try:
    # code that might cause an error
    print("I'm awsome!")
except ValueError:  
    print("That is not a valid number")
except ZeroDivisionError:
    print("You can't divide by 0")
except FileNotFoundError:
    print("There is no such file")
except TypeError:
    print("object of type 'int' has no len() OR SOME OTHER MESSAGE")
except PermissionError:
    print("You don't have permission!")
finally:
    # ALWAYS runs