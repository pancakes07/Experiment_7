"""class Mtd:
    def Fun(self,a,b):
        print("yo")
        print(a+b)
obj=Mtd()
obj.Fun(3,9)
obj.Fun(3.3,9.8)
obj.Fun("yo","nigga")"""

class Base:
    def Meth1(self):
        print("This is base class")

class Derived(Base):
    def Meth1(self):
        super().Meth1()
        print("This is derived class")

obj = Derived()
obj.Meth1()
