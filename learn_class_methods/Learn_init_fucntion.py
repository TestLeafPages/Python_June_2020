class testleaf:

    def __init__(self, name):
        self.name = name

    def python(self, aaa):
        self.aaa = aaa
        print(self.name)

    def devOps(self):
        print("for infra")
        print(self.name)
        print(self.aaa)



per1 = testleaf("Gopinath123")
per1.python()

per2 = testleaf("Babu123")
per2.python()

per3 = testleaf("Balaji123")
per3.python()


