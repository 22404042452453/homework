class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x,self.y)


pt = Point(4, 5)
print(pt.x,pt.y)
pt_2 = pt.clone()
print(pt_2.x,pt_2.y)
