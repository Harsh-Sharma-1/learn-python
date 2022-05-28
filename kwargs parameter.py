# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs): # we can use any name instead of kwargs but the ** are important that are used to pack the arguments to dictionary
   print('Hello',end=" ")
   for key,value in kwargs.items():
       print(value,end=" ")
   print()
       
hello(first="harsh",last="sharma")
hello(first="rajesh",middle="dinesh",last="sharma")