import random

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def grade(self):
        if self.score >= 70 and self.score <= 100:
            return "A"
        elif self.score >= 60 and self.score <= 70:
            return "B"
        elif self.score >= 40 and self.score <= 60:
            return "c"
        elif self.score >= 30 and self.score <= 40:
            return "D"
        else:
            return "F"
    
students = {}
name = []
for _ in range(10):
    name.append(input("write your name: "))

with open("name.txt", "a") as file:
    for n in name:
        file.write(f"{n}\n")

with open("name.txt", "r") as file:
    person = file.readlines()

for na in person:
    age = random.randrange(16,19)
    scores = random.randrange(20,100)
    students["Name"] = na.strip("\n")
    students["Score"] = scores
    students["Age"] = age
    st = Student(na,age,scores)
    students["Grade"] = st.grade()
    print(students)