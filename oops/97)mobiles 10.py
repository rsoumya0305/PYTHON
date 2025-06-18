class Mobile:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Mobile brand: {self.brand}"

m1 = Mobile("redmi")
m2 = Mobile("one plus")
m3 = Mobile("apple")
m4 = Mobile("samsung")
m5 = Mobile("nokia")

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
