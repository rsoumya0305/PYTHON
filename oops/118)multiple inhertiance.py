class C:
    def __init__(self):
        pass
    @staticmethod
    def language():
        print("i am python")
class Java:
    def __init__(self):
     super.__init__()
    @staticmethod
    def language():
        print("i am c lang")
class python(C,Java):
    def __init__(self):
      super.__init__()
    @staticmethod
    def language():
        print("i am jAVA lang")
C.language()
Java.language()
python.language()


