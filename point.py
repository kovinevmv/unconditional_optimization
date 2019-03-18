import numpy as np


class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, coef):
        return Point(self.x * coef, self.y * coef)

    def __str__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def to_matrix(self):
        return np.array([[self.x], [self.y]])

    def to_array(self):
        return np.array([self.x, self.y])


if __name__ == '__main__':
    pass
