# tuple => collection which is ordered and unchangeable used 
# to group together related data

student = ("harsh", 20, "male")
print(student.count("harsh"))
print(student.index("male"))

for x in student:
    print(x)
    
if "harsh" in student:
    print("harsh is here")
