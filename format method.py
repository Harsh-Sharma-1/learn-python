# str.format() =optional method that gives users more control when displaying output
animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) # positional arguments
print("The {ani} jumped {ani} over the {ite}".format(ani=animal,ite=item)) # keyword arguments

text = "The {} jumped over the {}"

print(text.format(animal,item))

# add padding to string using format
name = "Harsh"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you".format(name))
print("Hello my name is {:<10}. Nice to meet you".format(name)) # left align
print("Hello my name is {:>10}. Nice to meet you".format(name)) # right align
print("Hello my name is {:^10}. Nice to meet you".format(name)) # center align


# formal number

number = 3.14159
print("the number pi is {}".format(number))
print("the number pi is {:.2f}".format(number))

number2 = 1000
print("the number is {:,}".format(number2)) # to add comma at 1000
print("the number is {:b}".format(number2)) # to display the number as binary
print("the number pi is {:o}".format(number2)) # to display the number as octal
print("the number pi is {:X}".format(number2)) # hexadecimal
print("the number pi is {:E}".format(number2)) # scientific notation
