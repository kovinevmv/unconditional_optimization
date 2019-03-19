from functools import partial

import numpy as np
from numpy.linalg import inv
from scipy.optimize import minimize
from util.myPoint import Point

class Methods:
    def __init__(self, f_):
        self.function = f_
        self.step_len = 0
        self.step_count = 0
        self.start = Point(0, 0)

    def set_alpha(self, a):
        self.function.set_alpha(a)

    def set_step_len(self, len):
        self.step_len = len

    def set_step_count(self, count):
        self.step_count = count

    def set_start(self, start_):
        self.start = start_

    def grad_min(self, p, grad, a):
        return self.function.f(p - grad * a)

    def min_polak(self, x, p, a):
        return self.function.f(x + p * a)

    def gradient_descent_const_step(self):
        current_point = self.start
        res = [{
            'x': current_point.x(),
            'y': current_point.y(),
            'f(x,y)': self.function.f(current_point),
            'Кол-во выч. f': 1
        }]
        for i in range(self.step_count):
            grad = self.function.grad(current_point)
            current_point = current_point - grad * self.step_len

            value = self.function.f(current_point)
            if abs(value) < 1.7976931348623157e+150:
                res.append({
                    'x': current_point.x(),
                    'y': current_point.y(),
                    'f(x,y)': value,
                    'Кол-во выч. f': 1
                })
            else:
                break
        return res

    def gradient_descent_split_step(self):
        current_point = self.start
        res = [{
            'x': current_point.x(),
            'y': current_point.y(),
            'f(x,y)': self.function.f(current_point),
            'Кол-во выч. f': 1,
            'Размер шага': self.step_len
        }]
        f_calls = 1

        for i in range(self.step_count):
            if self.step_len < 1e-10:
                break

            step = self.step_len
            grad = self.function.grad(current_point)
            next = current_point - grad * step

            f_next = self.function.f(next)
            f_curr = self.function.f(current_point)
            f_calls += 2

            while f_next - f_curr > -step * 0.0001 * grad.dist():
                step *= 0.5
                next = current_point - grad * step
                f_next = self.function.f(next)
                f_calls += 1

            current_point = next
            res.append({
                'x': current_point.x(),
                'y': current_point.y(),
                'f(x,y)': f_next,
                'Кол-во выч. f': f_calls,
                'Размер шага': step
            })
            if abs(f_next) > 1.7976931348623157e+150:
                break
            f_calls = 0
        return res

    def gradient_descent_fast(self):
        current_point = self.start

        res = [{
            'x': current_point.x(),
            'y': current_point.y(),
            'f(x,y)': self.function.f(current_point),
            'Кол-во выч. f': 1
        }]

        for i in range(self.step_count):
            grad = self.function.grad(current_point)

            optfunc = partial(self.grad_min, current_point, grad)
            r = minimize(optfunc, 5, method='Nelder-Mead', options={'xtol': 1e-6})

            current_point = current_point - grad * r.x[0]
            f_calls = r.nit

            value = self.function.f(current_point)
            res.append({
                'x': current_point.x(),
                'y': current_point.y(),
                'f(x,y)': value,
                'Кол-во выч. f': f_calls
            })
            if abs(value) > 1.7976931348623157e+150 or abs(value - res[-2]['f(x,y)']) <= 1e-15:
                break
        return res

    def newton_raphson(self):
        current_point = self.start

        res = [{
            'x': current_point.x(),
            'y': current_point.y(),
            'f(x,y)': self.function.f(current_point),
            'Кол-во выч. f': 1
        }]

        for i in range(self.step_count):
            grad = self.function.grad(current_point).to_matrix()
            try:
                H = inv(np.matrix(self.function.grad2(current_point)))
            except:
                return res
            next = current_point.to_matrix() - H @ grad
            current_point = Point(next.item(0), next.item(1))
            value = self.function.f(current_point)

            res.append({
                'x': current_point.x(),
                'y': current_point.y(),
                'f(x,y)': value,
                'Кол-во выч. f': 1
            })

            if abs(value) > 1.7976931348623157e+150 or abs(value - res[-2]['f(x,y)']) <= 1e-15:
                break
        return res

    def polak_ribiere(self):
        current_point = self.start

        res = [{
            'x': current_point.x(),
            'y': current_point.y(),
            'f(x,y)': self.function.f(current_point),
            'Кол-во выч. f': 1
        }]

        prev_point = -1
        prev_p = 0

        for i in range(self.step_count):
            grad_current = self.function.grad(current_point)

            if i > 0:
                grad_prev = self.function.grad(prev_point)
                delta = (grad_current - grad_prev).to_array()
                beta = np.dot(delta, grad_current.to_array()) / grad_prev.dist() ** 2
                p_k = grad_current * -1 + prev_p * beta
            else:
                p_k = grad_current * -1

            optfunc = partial(self.min_polak, current_point, p_k)
            r = minimize(optfunc, 5, method='Nelder-Mead', options={'xtol': 1e-10})
            next = current_point + p_k * r.x[0]
            prev_point = current_point
            current_point = next
            prev_p = p_k

            value = self.function.f(next)
            res.append({
                'x': current_point.x(),
                'y': current_point.y(),
                'f(x,y)': value,
                'Кол-во выч. f': r.nit
            })
            if abs(value) > 1.7976931348623157e+150 or abs(value - res[-2]['f(x,y)']) <= 1e-32:
                break
        return res


if __name__ == '__main__':
    pass
