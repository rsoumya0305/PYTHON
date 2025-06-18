class Mobile:
    def __init__(self,colour,price,sries,version,featues,storage,brand,capacity,ram,rom):
        print("objects are created")
        self.Clr=colour
        self.Price=price
        self.Ser=sries
        self.Ver=version
        self.Fea=featues
        self.Str=storage
        self.Brand=brand
        self.Capacity=capacity
        self.Ram=ram
        self.Rom=rom
def display_details(self):
       print("details of employees are:")
       print({self.Clr})
       print({self.Price})
       print({self.Ser})
       print({self.Ver})
       print({self.Fea})
       print({self.Str})
       print({self.Brand})
       print({self.Capacity})
       print({self.Ram})
       print({self.Rom})
M1=Mobile("black","23000","i4",'33',"cam good","128gb","one plus","128gb",'12','14')
display_details(M1)
    