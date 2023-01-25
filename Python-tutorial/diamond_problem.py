
class A():
    def display(self):
        print("A class")

class B(A):
    pass

class C(A):
    pass

class D(C,B):
    pass

obj = D()
obj.display()