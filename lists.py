# list = used to store multiple items in a single variable

food = ["Pizza", "Hamburger", "Hotdog", "spaghetti"]

food[0] = "Sushi"

# print(food[0])

# adds a element in list
food.append("ice cream")

# removes a element from a list
food.remove("Sushi")

# removes the last element of the list
food.pop()

# insert a element at the specific index in the list
food.insert(0,"cake")

# sort a list
food.sort()


for x in food:
    print(x)
    
# clear a list
food.clear()
    
print(food)
    
    
