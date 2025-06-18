class Father():
    def __init__(self):
        pass                                              #method overriding
    @staticmethod
    def work():
        print("hard working")
class son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("ENJOYONG SON ")
class grandson(son):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("small boy")
Father.work()
son.work()
grandson.work()