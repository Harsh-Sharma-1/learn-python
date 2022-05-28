# Duck typing = concept where the class of an object is less important than the methods/attributes
# class type is not checked if minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, then it must be duck typing"

class Duck:
    def walk(self):
        print("this duck is walking")
    def talk(self):
        print("this duck is talking")
        
class Chicken:
    def walk(self):
        print("this chicken is walking")
    def talk(self):
        print("this chicken is talking")
        
class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")
        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
print()
person.catch(chicken)