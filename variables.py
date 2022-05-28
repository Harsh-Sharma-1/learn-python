# variable -> a container for a value. Behaves as the value that it contains similar as variables in algebra

name = "harsh" # this variable contains a string value a string is a series of charactors

print(name)
print("hello",name)
print(f"hello {name}")

first_name = "harsh"
last_name = "sharma"
full_name = first_name + last_name
print(full_name)
print(type(full_name))

#############################################################

# int value 
age = 19 
age = age + 1
age += 1
print(age)
print(type(age))

# to convert int to string we use age = str(age)

print(f"my name is {full_name} and my age is {age}")

############################################################

# float value
height = 250.3
print( "my height is " + str(height) + " cm")

############################################################

# boolean value
human = True
print("Are you a human :",human)
print(type(human))

