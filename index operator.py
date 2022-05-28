# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "Harsh Sharma"
if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:5].upper()
last_name = name[6:].lower()
last_charactor = name[-1]

print(first_name)
print(last_name)
print(last_charactor)


