# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

# to create a abstract class in python we need to import the abc module
from abc import ABC,abstractmethod

# abstract class
# an abstract class need to have atleast on abstract method
# the children of the abstract classes need to have implementation of abstract methods
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("you drive the car")
    
    def stop(self):
        print("this car is stopped")
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("your ride the motorcycle")
    
    def stop(self):
        print("this motorcycle is stopped")
        

car = Car()
motorcycle = Motorcycle()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()