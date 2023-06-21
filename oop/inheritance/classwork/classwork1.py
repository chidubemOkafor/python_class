class MyList:
    def __init__(self,data):
     self.intigers = data

    def get_item(self, index):
        return self.intigers[index]
    
    def get_slice(self,start,end):
        return self.intigers[start:end]
    
li = MyList([1,2,3,4,6,7,8])
print(li.intigers)
print(li.get_item(2))
print(li.get_slice(1,5))

# single inheritance
# multiple inheritance
# multilevel inheritance

