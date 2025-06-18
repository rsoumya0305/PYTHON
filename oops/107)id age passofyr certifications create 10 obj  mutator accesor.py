#initiaze without constructor
class student:
  def data(self,id,age,p,c):
    self.id=id
    self.age=age
    self.p=p
    self.c=c
    def Set_id(self):
        self.id="456"
    def Set_age(self):
        self.age="3456789"
    def Set_p(self):
        self.p="45"
    def Set_c(self):
        self.c="25"
    def Display(self):
        print(self.id)
        print(self.age)
        print(self.p)
        print(self.c)
id=input("enter id :")
age=input("enter age:")
p=input("enter p:")
c=input("enter c : ")
S1=id,age,p,c
print(S1)
S1.display()
S1.Set_id()
S1.Set_age()
S1.Set_p()
S1.Set_C()
S1.details()