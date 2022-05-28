try:
    with open('./assets/text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found")

    
#print(file.closed)