class A:

    def a(self):
        print("i'm from A")


class B(A):

    def b(self):
        print("i'm from B")


class C(B):

    def c(self):
        print("i'm from C")


cc = C()
cc.c()
cc.b()
cc.a()




