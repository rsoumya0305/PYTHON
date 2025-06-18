class Father():
    def __init__(self):
        pass
    @staticmethod
    def work():
        print("hard working")
class son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("ENJOYONG SON ")
Father.work()
son.work()
    