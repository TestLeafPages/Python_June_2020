class A:

    def a(self):
        print("i'm from A")


class B:

    def b(self):
        print("i'm from B")


class C(B, A):

    def c(self):
        print("i'm from C")

aa = A()
aa.a()

bb  = B()
bb.b()

cc = C()
cc.c()
cc.b()
cc.a()



