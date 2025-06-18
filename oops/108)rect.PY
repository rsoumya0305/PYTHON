'''RECTANGLE CLASS AND INITILIZE VARIABLES LEN,BREATH USINNG CONDTRUCTOR AND ACCESS USING MUTATATOR METHOD'''
class Rectangle:
    def __init__(self, length, breadth):
        # Constructor to initialize values
        self.length = length
        self.breadth = breadth

    # Mutator methods (setters)
    def set_length(self, length):
        self.length = length

    def set_breadth(self, breadth):
        self.breadth = breadth

    # Accessor methods (getters)
    def get_length(self):
        return self.length

    def get_breadth(self):
        return self.breadth

    # Method to calculate area
    def area(self):
        return self.length * self.breadth


# ---------- Main Program ----------

# Create rectangle object with initial values
r1 = Rectangle(10, 5)

# Update using mutators
r1.set_length(12)
r1.set_breadth(6)

# Access and display using accessors
print("Length:", r1.get_length())
print("Breadth:", r1.get_breadth())
print("Area:", r1.area())
