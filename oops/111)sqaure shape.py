'''Write a Python Program to Create a SquareShape class & declare the propert as

Length

Breadth

Height

1) Calculate the Area of Square

11) Check Whether the Sides of Square's are equal or not

iii) Calculate the Perimeter of Square

iv) Find the Diagonals of Square'''
import math
class square:
    def __init__(self,length,breadth):
       self.length=int(length)
       self.breadth=int(breadth)
    
    def display(self):
        print(self.length)
        print(self.breadth)
 
    def area(self):
        return self.length*self.breadth
    def side(self):
        if(self.length==self.breadth):
           return True 
        return False  
    def perimeter(self):
        return 4*self.length
    def diagonal(self):
        return self.length*math.sqrt(2)
s1=square("20","30",)
s1.display()
print("Area:", s1.area())
s1.side()
print("side:", s1.side())
s1.perimeter()
print("perimeter:", s1.perimeter())