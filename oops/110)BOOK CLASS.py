'''Write a Python Program to Create a Book Class declare the states as

BookName

AuthorName

Publisher Name

PublishedDate

Category Of Book

1) Create 5 Objects & Initialize the Values Using Constructor where out of five

--Create 1st Object using one parameterized Constructor

--Create 2nd Object using Two parameters Constructor

--Create 3rd Object using zero parameterized Constructor

--Create 4th Object using four parameters Constructor

--Create 5th Object using Five parameters Constructor

11) Access the Values using Accessor Methods

111) Update

Activate

class Book:
    def __init__(self,name=0,author=0,publisher=0,date=0,category=0):
        self.name=name
        self.author=author
        self.publisher=publisher
        self.date=date
        self.categery=category
    def display(self):
        print(self.name)
    def author(self):
        print(self.author)
    def publisher(self):
        print(self.publisher)
    def date(self):
        print(self.date)
    def category(self):
        print(self.category)
    def get(self):
            


s1=Book("physics")
s2=Book("soumya","safi")
s3=Book()
s4=Book("15","16","17","18")
s5=Book("study","rlsoumya","safi","pri","dfg")

s1.display()
s2.author()
s3.publisher()
s4.date()
s5.category()'''

class Book:
    def __init__(self, name=None, author=None, publisher=None, date=None, category=None):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.date = date
        self.category = category

    # Accessor (Getter) Methods
    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_date(self):
        return self.date

    def get_category(self):
        return self.category

    # Display all details
    def display(self):
        print("Book Details:")
        print("Name:", self.name)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
        print("Published Date:", self.date)
        print("Category:", self.category)
        print("----------------------------")

# Creating 5 objects with different number of parameters
book1 = Book("Physics")                                           # 1 parameter
book2 = Book("Python Programming", "Soumya")                      # 2 parameters
book3 = Book()                                                    # 0 parameters
book4 = Book("Data Science", "Anita", "TechBooks", "2022")        # 4 parameters
book5 = Book("Machine Learning", "Ravi", "O'Reilly", "2023", "Tech")  # 5 parameters

# Access values using accessor methods
print("Accessor Methods Output:")
print("Book 1 Name:", book1.get_name())
print("Book 2 Author:", book2.get_author())
print("Book 4 Publisher:", book4.get_publisher())
print("Book 5 Date:", book5.get_date())
print("Book 5 Category:", book5.get_category())
print()

# Displaying all books
print("Displaying All Book Details:")
book1.display()
book2.display()
book3.display()
book4.display()
book5.display()

# 🔁 Updating Book 3's values directly (no update method used)
book3.name = "Artificial Intelligence"
book3.author = "John McCarthy"
book3.publisher = "AI Books Inc."
book3.date = "2025"
book3.category = "Technology"

# Display updated book3
print("After Direct Update of Book 3:")
book3.display()

