# the class Point takes in the coordinate x,y,
# First method is plot_point that prints the position of point.
# Second method is calculate_dist which takes in x and y from another point, and returns the distance calculated between two points.

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
        

point1 = Point(3,4) ## point1 is an object of this class
point1.plot_point()

point1.calculate_dist(7,4) ## with method calculate_dist this calculates the distance between (7,4) and point1

