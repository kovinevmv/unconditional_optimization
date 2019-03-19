import numpy as np
from myPoint import Point

class Function:
    def __init__(self):
        self.alpha = 0

    def set_alpha(self, a):
        self.alpha = a

    def f(self, x, y=None):
        if y is None:
            return np.power((x.y() - np.power(x.x(), 2)), 2) + self.alpha * np.power((x.x() - 1), 2)
        else:
            return np.power((y - np.power(x, 2)), 2) + self.alpha * np.power((x - 1), 2)

    def _dx(self, p):
        return 4 * p.x() * (np.power(p.x(), 2) - p.y()) + 2 * self.alpha * (p.x() - 1)

    def _dy(self, p):
        return 2 * (p.y() - np.power(p.x(), 2))

    def _dxdx(self, p):
        return 12 * np.power(p.x(), 2) - 4 * p.y() + 2 * self.alpha

    def _dxdy(self, p):
        return -4 * p.x()

    def _dydy(self, p):
        return 2

    def grad(self, p):
        return Point(self._dx(p), self._dy(p))

    def grad2(self, p):
        return np.array([[self._dxdx(p), self._dxdy(p)], [self._dxdy(p), self._dydy(p)]])


if __name__ == '__main__':
    pass
