import numpy as np
from PyQt5.QtCore import QPointF


class Point(QPointF):
    def __init__(self, x, y):
        super(QPointF, self).__init(x, y)

    def x(self):
        return self._p.x()

    def y(self):
        return self._p.y()

    def dist(self):
        return (self._p.x() * self._p.x() +
                self._p.y() * self._p.y()) ** 0.5

    def to_matrix(self):
        return np.array([[self._p.x()], [self._p.y()]])

    def to_array(self):
        return np.array([self._p.x(), self._p.y()])
