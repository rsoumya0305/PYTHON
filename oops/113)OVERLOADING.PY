#EMPLOYEE DIFEERENT STATES 5 OBJECTS USING CONSTRUCTOR

'''class Employee():

    def __init__(self,*arg):
        print("objects are created")
    if(self,*args)
        self.EmpName=emp
        self.Designation=des
        self.Salary=salary
        self.location=location
        self.dept=dept
        print("5 parameters are constructor")
    
    def __init__(self,emp,des,salary,location):
        print("objects are created")
        self.EmpName=emp
        self.Designation=des
        self.Salary=salary
        self.location=location
        print("4 parameters are constructor")

    def __init__(self,emp,des,salary):
        print("objects are created")
        self.EmpName=emp
        self.Designation=des
        self.Salary=salary   
        print("3 parameters are constructor")

    def __init__(self,emp,des):
        print("objects are created")
        self.EmpName=emp
        self.Designation=des
        print("2 parameters are constructor")

    def __init__(self,emp):
        print("objects are created")
        self.EmpName=emp
        print("1 parameters are constructor")

    def __init__(self):
        print("i am 0 paramaterized")
e1=Employee("sou","234","gun","2500")'''

class Employee:
    def __init__(self, emp=None, des=None, salary=None, location=None, dept=None):
        self.EmpName = emp
        self.Designation = des
        self.Salary = salary
        self.Location = location
        self.Dept = dept

    def display(self):
        print(f"Name: {self.EmpName}, Designation: {self.Designation}, Salary: {self.Salary}, Location: {self.Location}, Department: {self.Dept}")
# Object with 1 parameter
e1 = Employee("Ravi")

# Object with 2 parameters
e2 = Employee("Anita", "Manager")

# Object with 3 parameters
e3 = Employee("John", "Developer", 50000)

# Object with 4 parameters
e4 = Employee("Sara", "Tester", 40000, "Hyderabad")

# Object with 5 parameters
e5 = Employee("Kiran", "Analyst", 60000, "Mumbai", "Finance")

# Display info
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()
