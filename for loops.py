# for loop = a statement that will execute it's block of code a limited 
# amount of times

import time

for i in range(10):
    print(f"Hello {i+1}")
    
print("")

for i in range(2,8,2):
    print(f"Hello {i}")
    
print("")

#for i in "Bro Code":
#    print(i)
    
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)

print("Count down completed")