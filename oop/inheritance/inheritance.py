class Animal:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def __init__(self, name, age): #constructure
        Animal.__init__(self,name,age) #constructure
    def eat(self):
        print(f"the {self.age} years old dog {self.name} is eating a bone")

bull_dog = Dog("bull dog",20)
bull_dog.eat()
