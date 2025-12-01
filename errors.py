# syntax for try-catch error thingy


try:
    # code that might cause an error
    print("I'm awsome!")
except ValueError:  
    raise ValueError("That is not a valid number")
except ZeroDivisionError:
    raise ZeroDivisionError("You can't divide by 0")
except FileNotFoundError:
    raise FileNotFoundError("There is no such file")
except TypeError:
    raise TypeError("object of type 'int' has no len() OR SOME OTHER MESSAGE")
except PermissionError:
    raise PermissionError("You don't have permission!")
finally:
    # ALWAYS runs