class A:

    def a(self):
        print("i'm from A")


class B(A):

    def b(self):
        print("i'm from B")


aa = A()
aa.a()


bb = B()
bb.b()
bb.a()

