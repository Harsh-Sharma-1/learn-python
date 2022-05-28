class Animal:
    def eat(self):
        print("This animal is eating")
        
class Rabbit(Animal):
    
    # now we will use this eat method instead of the one thats provided by the animal
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()