# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

# class Manager(Employee):
#     def __init__(self, name, salary, bonus = 10):
#         Employee.__init__(self, name, salary)
#         self.bonus = bonus
#         self.value = (self.salary * self.bonus) / 100
#         self.salary += self.value
       
# class Engineer(Employee):
#     def __init__(self, name, salary, bonus = 15):
#         Employee.__init__(self, name, salary)
#         self.bonus = bonus
#         self.value = (self.salary * self.bonus) / 100
#         self.salary += self.value

# def payroll(profile):
#     name_salary = {}
#     for pro in profile:
#         if profile[pro]["occupation"] == "engineer":
#             management = Engineer(pro,profile[pro]["salary"])
#         elif profile[pro]["occupation"] == "manager":
#             management = Manager(pro,profile[pro]["salary"])  
#         name_salary[management.name] = int(management.get_salary())
#     print(name_salary)

# payroll({
#     "james": {"salary": 5000, "occupation": "engineer"},
#     "john": {"salary": 6000, "occupation": "manager"},
#     "mary": {"salary": 5000, "occupation": "manager"}
#     })
    

