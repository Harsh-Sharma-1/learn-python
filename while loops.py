# while loop = a statement that will execute it's block of code 
# as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter you name: ")

print(f"Hello {name}")

print(bool(""))