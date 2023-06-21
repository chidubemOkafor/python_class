class Animal:
    def __init__(self, name, age, gender, children):
        self.name =  name
        self.age = age
        self.sex = gender
        self.children = children

    def sound(self):
        if self.name == "cat":
            print("Meow")
        elif self.name == "dog":
            print("bark")
        else:
            print("Don't know sound")

    def profile(self):
        if self.sex == "male":
            self.pronoun = "he's"
            self.parent = "father"
        else:
            self.pronoun = "she's"
            self.parent = "mother"
        print(f"My {self.name} is a {self.sex} and {self.pronoun} a {self.age} years old {self.parent} of {self.children}")

    def getProfile(self):
        self.profile()

dog = Animal("dragon",1000,"male", 10)

dog.profile()
