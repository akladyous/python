class A:
    def __init__(self):
        print("class A")

class B(A):
    def __init__(self):
        print("class B")
        super(B, self).__init__()

class C(B):
    def __init__(self):
        print("class C")
        super(C, self).__init__()

x=C()
print(C.mro())