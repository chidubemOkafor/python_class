class Manager:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def profile(self):
        return f"{self.name} get paid ${self.salary}"
    
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def profile(self):
        return f"{self.name} get paid ${self.salary}"
    
john = Manager("john", 20000)
james = Employee("james", 2000)

management = [john, james]

for members in management:
    print(members.profile())