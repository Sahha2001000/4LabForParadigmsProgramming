class Rectangle(object):
    def __init__(self, height=2, width=3):
        self.height = height
        self.width = width

    def meetUser(self):
        print("\nThis program help find you perimeter and square your rectangle")
        return 1

    def findPerimeter(self):
        a = self.height
        b = self.width
        if (a <= 100) and (b <= 100):
            if (a == b):
                p = a * 4
            else:
                p = 2 * (a + b)
            return p
        else:
            return "Height and width must be <= 100"

    def findSquare(self):
        a = self.height
        b = self.width
        if (a <= 100) and (b <= 100):
            if (a == b):
                s = a * a
            else:
                s = a * b
            return s
        else:
            return "Height and width must be <= 100"

    def outputRectangle(self, p, s, userChoose=3):
        if (userChoose == 1):
            print(f"\nSquare your rectangle: {s}")
            return 1
        elif (userChoose == 2):
            print(f"\nPerimeter your rectangle: {p}")
            return 1
        else:
            print(f"\nSquare your rectangle: {s}")
            print(f"\nPerimeter your rectangle: {p}")
            return 1
