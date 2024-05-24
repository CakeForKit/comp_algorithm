from matplotlib import pyplot as plt
from slauNewton import newton_slau
from numpy import linspace

# y'' - y**3 = x**2
X0, Y0 = 0, 1
X1, Y1 = 1, 3
N = 100
step = (X1 - X0) / N
EPS = 1e-5


def beg_y(x):
    return 2 * x ** 1 + 1


# n-я функция для разностной замены
def f(n, N, step, x: list):
    if n == 0:
        def resf(*y):
            return y[0] - Y0
    elif n == N:
        def resf(*y):
            return y[n] - Y1
    else:
        def resf(*y):
            return (y[n - 1] + -2 * y[n] + y[n + 1]) / (step ** 2) - y[n] ** 3 - x[n] ** 2
    return resf


# y - приближенные значения, step = h в формуле
# матрица якоби для разностного аналога
def jacobian(*y):
    N = len(y)
    res = []
    res.append([1] + [0] * (N - 1))
    for i in range(1, N - 1):
        res.append([0] * (i - 1) +
                   [1 / (step ** 2)] +
                   [-2 / (step ** 2) - 3 * (y[i] ** 2)] +
                   [1 / (step ** 2)] +
                   [0] * (N - i - 2))
    res.append([0] * (N - 1) + [3])  # [1]???
    return res


def draw_graphic(x_vals, y_vals, y0_vals):
    plt.figure("График функции")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)

    plt.plot(x_vals, y_vals, 'b', label="y'' - y**3 = x**2")
    plt.plot(x_vals, y0_vals, 'g', label="2 * x ** 2.2 + 1")

    plt.legend()
    plt.show()


if __name__ == '__main__':
    x_vals = list(linspace(X0, X1, N + 1))
    funcs = [f(i, N, step, x_vals) for i in range(N + 1)]
    y0_vals = [beg_y(x) for x in x_vals]

    y_vals = newton_slau(jacobian, funcs, y0_vals, EPS)
    draw_graphic(x_vals,  y_vals, y0_vals)

    print(y_vals[-2])
