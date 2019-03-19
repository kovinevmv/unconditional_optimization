import numpy as np
from PyQt5.QtCore import QPointF


class Point(QPointF):
    def __init__(self, x, y):
        super(QPointF, self).__init__(x, y)

    def __add__(self, other):
        return Point(other.x() + self.x(), other.y() + self.y())

    def __sub__(self, other):
        return Point(self.x() - other.x(), self.y() - other.y())

    def __mul__(self, other):
        return Point(self.x() * other, self.y() * other)

    def __pow__(self, other):
        return Point(self.x() ** other, self.y() ** other)

    def __str__(self):
        return f'Point({self.x()}, {self.y()})'

    def dist(self):
        return (self.x() ** 2 + self.y() ** 2) ** 0.5

    def to_matrix(self):
        return np.array([[self.x()], [self.y()]])

    def to_array(self):
        return np.array([self.x(), self.y()])


if __name__ == '__main__':
    pass