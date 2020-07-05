class A:
    ls = []
    def __init__(self):
        print(self.ls)

    def __init__(self, *args):
        self.ls = args
        print(self.ls)


per1 = A(1, 2, 3, 4, 5)
per2 = A(10, 20 ,30)