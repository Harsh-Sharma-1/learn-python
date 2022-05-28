# *args => parameter that will pack all arguments into a tuple 
# useful so that a function can accept a varying amount of arguments

def add(*args): # we can use any name instead of args but the * is important it is used for packing all the arguments into a tuple
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,2,4,5,6))