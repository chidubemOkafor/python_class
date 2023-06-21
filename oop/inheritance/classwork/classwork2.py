# write a class that takes a dictionary that has three function
#1.get a sum of people that submited
#2.grade them and this should return a new dictionary
#3.get the average and assign

class Grade:
    def __init__(self,dictionary):
        self.dictionary = dictionary
    def Counter(self):
        count = 0
        for i in self.dictionary:
            count += 1 
        return count
    
    def Grade(self):
        grade_dictionary = {}
        for i in self.dictionary:
            print(i)
            if self.dictionary[i] >= 70:
                grade_dictionary[i] = "A"
            elif self.dictionary[i] > 60 and self.dictionary[i] < 69:
                grade_dictionary[i] = "B"
        return grade_dictionary

db = Grade({"john": 67, "mary": 70 })
print(db.Grade())

