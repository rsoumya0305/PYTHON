'''write a python program to create a product class declare the states of the class 
as product name , product id, price,gst,manufacture date expired date
create five obj initialised using paarameterized constructor accese elements
 using instance method and declare mutator methods as set product name set product price 
for all and change the values of their properties using mutator mrthods and printened'''
class Product():
    def __init__(self,n,id,price,gst,md,exd):
        self.Name=n
        self.Id=id
        self.Price=price
        self.Gst=gst
        self.Md=md
        self.Exd=exd
    def Set_Name(self):
        self.Name="soap"
    def Set_Id(self):
        self.Id="2345"
    def Set_Price(self):
        self.Price="3456789"
    def Set_Gst(self):
        self.Gst="45"
    def Set_Md(self):
        self.Md="7-06-2025"
    def Set_Exd(self):
        self.Exd="11-10-2025"
    def details(self):
        print(self.Name)
        print(self.Id)
        print(self.Price)
        print(self.Gst)
        print(self.Md)
        print(self.Exd)
P1=Product("shampoo","23hjk","2344467","30","10-06-2025","12-12-2025")
P1.details()
print("after changing")
P1.Set_Name()
P1.Set_Id()
P1.Set_Price()
P1.Set_Gst()
P1.Set_Md()
P1.Set_Exd()
P1.details()
