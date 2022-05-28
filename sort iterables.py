# sort() method = used with lists
# sort() function = used with iterables

students = ["Harsh", "Rajesh", "Suresh", "Ramesh", "Akash", "Dinesh"]

# sort method
students.sort()
for i in students:
    print(i)

print()

# sort method only work with list
# it does not work with tuple
students.sort(reverse=True)
for i in students:
    print(i)
print()

# sort function => this function returns a sorted lists

sorted_students = sorted(students)
# sorted_students = sorted(students,reverse=true)
for i in sorted_students:
    print(i)
    print()


# sort a list of tuple
students_data = [("Rajesh", "F", 60),
                 ("Harsh", "A", 100),
                 ("Mahesh", "C", 70),
                 ("Dinesh", "B", 105),
                 ]

students_data.sort()  # by default the list will get sort by the first column
for i in students_data:
    print(i)
print()

# to sort by grade


def grade(grades): return grades[1]


students_data.sort(key=grade)
for i in students_data:
    print(i)
print()


def mark(marks): return marks[2]


# using sorted function to sort
sorted_students_data = sorted(students_data, key=mark)
for i in sorted_students_data:
    print(i)
print()
