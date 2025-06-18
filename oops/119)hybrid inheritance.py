class hi():
    def __init__(self):
        pass
    @staticmethod
    def bye():
        print('i am hii')
class helo(hi):
    def __init__(self):
        pass
    @staticmethod
    def bye():
        print('i am helo')
class bye(hi):
    def __init__(self):
        pass
    @staticmethod
    def bye():
        print('i am bye')
class ok(helo,bye):
    def __init__(self):
        pass
    @staticmethod
    def bye():
        print('i am ok')
helo.bye()
hi.bye()
bye.bye()
ok.bye()


