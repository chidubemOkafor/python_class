#overiding
class Organization:
    def __init__(self, org_name):
        self.org_name = org_name

class Employee1(Organization):
    def __init__(self, age, ename, org_name):
        Organization.__init__(self, org_name)
        self.employee = ename
        self.age = age

class Employee2(Organization):
    def __init__(self, age, ename, org_name):
        Organization.__init__(self,org_name)
        self.employee = ename
        self.age = age

class Height1:
    def __init__(self, height):
        self.height = height

class Height2:
    def __init__(self, height):
        self.height = height

class Manager(Employee1, Employee2, Height1, Height2):
    def __init__(self, age1, age2, ename1, ename2, org_name, height1, height2):
        Employee1.__init__(self, age1, ename1, org_name)
        Employee2.__init__(self, age2, ename2, org_name)
        Height1.__init__(self, height1)
        Height2.__init__(self, height2)

james = Manager(20,30,"tom","jerry","microsoft","130cm","300cm")
print(james.employee)
print(james.age)
print(james.height)