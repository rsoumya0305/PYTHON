class vehical:
    def __init__(self):
        print("i am the vehical class constructor")
    '''@staticmethod
    def start():
        print("car is started")'''
class car(vehical):
    def __init__(self):
        super().__init__()
        print("i am the car class constructor")

c1=car()
#c1.start()