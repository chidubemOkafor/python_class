class Rectangle:
    def __init__ (self):
        self.width = 100
        self.height = 100

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height)*2
    
    def scale(self,n):
        self.height *= n
        self.height *= n

rectangle = Rectangle()
area = rectangle.area()
perimeter = rectangle.perimeter()
print(area)
print(perimeter)
