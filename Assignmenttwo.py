class Rectangle: 
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Width: {}, Height: {}, Area: {}, Perimeter: {}".format(self.width, self.height, self.getArea(), self.getPerimeter())

width = 3
height = 30
width2 = 4.5
height2 = 45.5
rectanle1=Rectangle(width, height)
rectanle2=Rectangle(width2, height2)
print(rectanle1)
print(rectanle2)
print("Ratio: {}".format(rectanle1.getArea() / rectanle2.getArea()))
