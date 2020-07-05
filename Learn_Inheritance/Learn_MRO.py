class Gp1:

    def get_gp1(self):
        print("from Gp1")


class Gp2:

    def get_gp2(self):
        print("from Gp2")


class A(Gp1, Gp2):

    def a(self):
        print("i'm from A")


class B:

    def com(self):
        print("from B")

    def b(self):
        print("i'm from B")


class C(A, B):

    def c(self):
        print("i'm from C")


cc = C()
cc.com()

print(C.mro())





