import math

class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def plot_pint(self):
        print(" Coordinates are ", "(",self.x, ",", self.y,")")

    def calculate_dist(self,x1,y1):
        distance = math.sqrt((self.x-x1)**2 + (self.y-y1)**2)
        print(distance)

point1 = Point(3,4)
point1.plot_pint()
point1.calculate_dist(7,4)

