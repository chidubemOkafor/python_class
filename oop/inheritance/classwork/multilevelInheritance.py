class Company:
    def __init__(self, company_name):
        self.company = company_name

    def profile(self):
        return self.company

class Work(Company):
    def __init__(self,occupation,company):
        super().__init__(company)
        self.occupation = occupation

    def worker(self):
        return f"your occupation in {self.company} is {self.occupation} {self.salary}"

class Employee(Work):
    def __init__(self, salary,occupation,company):
        super().__init__(occupation,company)
        self.salary = salary

    def Employee_profile(self): 
       return f"your occupation in {self.company} is an {self.occupation} and you earn {self.salary}"

bt = Employee(100,"engineer","microsoft")
print(bt.Employee_profile())
     