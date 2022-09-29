a, b, c = map(int, input().split())


class TriangleChecker():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return 2
        else:
            return 3


tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
