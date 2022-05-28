# lambda functions = function written in 1 line using lambda keyword
#                    accepts any number of arguments, but only has one expression
#                    (think of it as a shortcut)
#                    (useful if needed for a short peroid of time, throw-away)

# lambda parameters:expression

#def double(x):
#    return x * 2

double = lambda x:x*2
print(double(5))

multiply = lambda x,y:x*y
print(multiply(5,6))

add = lambda x,y,z:x+y+z
print(add(1,2,3))

full_name = lambda first_name,last_name:first_name +" "+last_name
print(full_name("Harsh","Sharma"))

age_check = lambda age:True if age>=18 else False

print(age_check(21))