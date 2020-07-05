class A:

    def a(self, *args):
        print("i'm from A")

    def z(self):
        pass


class B(A):

    def b(self):
        print("i'm from B")

    def a(self, x, y):
        print('implemented ABS')

bb = B()
bb.a()