class A:
    def __new__(cls):
        x=super(A, cls).__new__(cls)
        print("A: ",x)
        return x
    def m(self):
        print("m of A called")

class B(A):
    def __new__(cls):
        x=super(B, cls).__new__(cls)
        print("B: ",x)
        return x
    def m(self):
        print("m of B called")
    
class C(A):
    def __new__(cls):
        x=super(C, cls).__new__(cls)
        print("C: ",x)
        return x    
    def m(self):
        print("m of C called")

class D(B,C):
    def __new__(cls):
        x=super(D, cls).__new__(cls)
        print("D: ",x)
        return x
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

x = D()
B.m(x)
C.m(x)
D.m(x)