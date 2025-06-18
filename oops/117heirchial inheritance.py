class python():
    def __init__(self):
        pass
    @staticmethod
    def language():
        print("i am python")
class c(python):
    def __init__(self):
     super.__init__()
    @staticmethod
    def language():
        print("i am c lang")
class java(python):
    def __init__(self):
      super.__init__()
    @staticmethod
    def language():
        print("i am jAVA lang")
python.language()
c.language()
java.language()
 
    
