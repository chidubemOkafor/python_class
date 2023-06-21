class Father:
    def __init__(self, fname):
        self.father_name = fname
    def fathers_occupation(self):
        print(f"my father's name is {self.father_name} and he is an Engineering")

class Mother:
    def __init__(self, mname):
        self.mother_name = mname
    def mothers_occupation(self):
        print(f"my mother's name is {self.mother_name} and she is a nurse")

class Brother:
    def __init__(self, bname):
        self.brother_name = bname
    def brothers_occupation(self):
        print(f"my brother's name is {self.brother_name} and he is a teacher")
        

class child(Father,Mother,Brother):
   def __init__(self, fname,mname,bname):
      Father.__init__(self,fname)
      Mother.__init__(self,mname)
      Brother.__init__(self, bname)

john = child("david","mary","wale")
john.fathers_occupation()
john.mothers_occupation()
john.brothers_occupation()