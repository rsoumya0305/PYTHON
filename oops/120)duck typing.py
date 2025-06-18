class duck:
    def walk(self):
        print("tapak,tappak")
class horse:
    def walk(self):
        print("dapp,dappa")
def myfunction(obj):
    obj.walk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)