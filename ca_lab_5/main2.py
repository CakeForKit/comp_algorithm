import math as m
from matplotlib import pyplot as plt
from numpy import linspace

def trapezoid_method_0_x(func, x_steped):
    integral = 0
    for i in range(len(x_steped) - 1):
        a, b = x_steped[i], x_steped[i + 1]
        integral += (b - a) * (func(a) + func(b)) / 2

    return integral


def laplas(x, n=100):
    def func(x):
        return m.exp(-x ** 2 / 2)

    x_steped = linspace(0, x, n)
    integral = trapezoid_method_0_x(func, x_steped)
    return 2 / m.sqrt(2 * m.pi) * integral


def half_div(func, a, b, eps):
    mid = (a + b) / 2
    while abs(func(mid)) > eps:
        if func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid
        mid = (a + b) / 2
    return mid

def draw_graphic():
    a, b, eps = -3, 3, 1e-5
    root = half_div(laplas, a, b, eps)
    print(f'root = {root:.20f}')

    x_vals = list(linspace(-3, 3, 300))
    y_vals = [laplas(i) for i in x_vals]

    plt.figure("График функции")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)

    plt.plot(root, laplas(root), 'r.')
    plt.plot(x_vals, y_vals, 'b', label="y = laplas")

    plt.legend()
    plt.show()


if __name__ == '__main__':
    draw_graphic()
