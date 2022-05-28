# Higher order functions = a. functions that either
#                   1. accepts a function as an argument
#                       or
#                   2. returns a functions
#                   (In python, functions are also treated as objects)


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# appects function as a argument
def hello(func):
    text = func("Hello")
    print(text)
    
hello(loud)
hello(quiet)

# returns a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

print(divisor(2)(8))

