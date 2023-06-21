# public member are accessible from anywhere in the class
# private members are not accessibke from anywhere in the class "__"
# protected member is prifixed by a single underscore "_"


#protected
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary

# class Work(Employee):
#     def __init__(self,name,salary,work):
#         super().__init__(name,salary)
#         self.work = work
# protected = Work("mike",2000,"engineer")
# print(protected._salary)

#private
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
# private = Employee("david",10000)
# print(private.__salary)

#private (1.to access it)
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary
# private = Employee("david",10000)
# print(private.get_salary())

#private(2.to access it)
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
        
#     def get_salary(self):
#         print(self.__salary)

# john = Employee("john", 100000)
# print(john._Employee__salary)


