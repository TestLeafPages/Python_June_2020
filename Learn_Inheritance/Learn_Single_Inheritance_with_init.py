class A:

    def __init__(self):
        print('__init__ frm A')

    def a(self):
        print("i'm from A")


class B(A):

    def __init__(self):
        print('__init__ frm B')
        super().__init__()

    def b(self):
        print("i'm from B")

bb = B()


