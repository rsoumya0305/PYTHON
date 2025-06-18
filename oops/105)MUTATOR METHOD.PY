class Mobile:
    def __init__(self,p,c,b):
        self.Price=p
        self.Colour=c
        self.Brand=b
        print("OBJECTS ARE:")
    def Set_Colour(self):
        self.Colour="blue"  #MUTATOR
    def Details(self):
        print(self.Price)
        print(self.Colour)
        print(self.Brand)
  
M1=Mobile("2300","black","samsung")
M1.Details()
print("after changing:")
M1.Set_Colour()
M1.Details()
    