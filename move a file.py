import os
source = "./assets/move.txt"
destination = "./assets/move test/move.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source,"was moved")
except FileNotFoundError:
    print(source+ " was not found")