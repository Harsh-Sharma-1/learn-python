# scope = the region that a variable is recognized 
# a variable is only available from inside the region it is created
# a global and locally scoped versions of a variable can be created

name = "harsh" # global scope (available inside and outside a function)

def display_name():
    name='sharma' # local scope (available only inside the function)
    print(name)
  
print(name) # cannont be used 
display_name()

# LEGB => Local => Enclosing => Global => Built-in
