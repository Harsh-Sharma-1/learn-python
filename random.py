import random

x = random.randint(1,6) # random number from a range
y = random.random() # random floating point number

mylist = ["Rock","Paper","Scissors"]
z = random.choice(mylist) # random element from list


cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards) # shuffle the list

print(x)
print(y)
print(z)
print(cards) 