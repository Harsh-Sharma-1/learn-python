class Car:
    # class variable declared inside the class but outside the function
    #class variable    
    wheels = 4
    
    def __init__(self,make,model,year,color):
        # instance variable
        self.make = make 
        self.model = model
        self.year = year
        self.color = color
        

Car.wheels = 2 # to change the value of class variable using class itself

print(Car.wheels)