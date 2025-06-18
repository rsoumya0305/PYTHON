class Employee():
    def __init__(self,emp,des,salary):
        print("objects are created")
        self.EmpName=emp
        self.Designation=des
        self.Salary=salary
    def display_details(self):
        print({self.EmpName})
        print({self.Designation})
        print({self.Salary})
E1=Employee("SOU",'data analsyt',25000)
E1.display_details()
E1.display_details()
E1.display_details()
E1.display_details()


