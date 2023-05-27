class Point:
    _counter = 0
    _lista=None
    
    def __new__(cls, *args, **kwargs):
        if (not cls._lista):
            cls._lista=[]

        istanza = super(Point, cls).__new__(cls)
        cls._counter += 1
        cls._lista.append(istanza)
        return istanza
    # ----------------------------------------------------------------
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    # ----------------------------------------------------------------
    def __str__(self):
        return f"point {self.x}, {self.y}"

    # def __add__(p1, p2):
    #     return Point(p1.x + p2.x, p1.y + p2.y)
# ----------------------------------------------------------------
p1=Point(1,2)
print(f"contatore al p1 {Point._counter}")
p2=Point(3,4)
print(f"contatore a2 p1 {Point._counter}")
print(p1)
print(p2)
print(p1+p2)
print(f"contatore al p3 {Point._counter}")


