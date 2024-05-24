from numpy import linspace, exp, log

from gauss_integral import gauss_integral
from sympson_integral import sympson_integral
from work_data import read_data, generate_data_by_func
from spline_func import spline_f_xy_
from tab_diff import tab_diff

# y = 1 - x, x = 0, y = 0
# OX [0, 1 - y]
# OY [0, 1]

EPS = 1e-5
FILENAME = 'data/data.txt'


def func1(x, y):
    return x * y


def func2(x, y):
    return x ** 2 + y ** 2 + 1


def func3(x, y):
    return exp(2 * x) * y


def test_spline():
    test_func = func2
    x_vals, y_vals, z_vals = generate_data_by_func(test_func, -1, 1, -1, 1, 0.05)
    spline_func = spline_f_xy_(x_vals, y_vals, z_vals)

    print('-' * len(linspace(min(x_vals), max(x_vals), len(x_vals) * 3)))
    for x in linspace(min(x_vals), max(x_vals), len(x_vals) * 3):
        for y in linspace(min(y_vals), max(y_vals), len(y_vals) * 3):
            if abs(test_func(x, y) - spline_func(x, y)) > 1e-3:
                print(f'spline error: {test_func(x, y) - spline_func(x, y):.10f}, x={x}, y={y}')
        print('-', end='')
    print()


def get_integral(use_func, nx, ny):
    def F(y):
        def f(x):
            return use_func(x, y)

        return gauss_integral(0, 1 - y, nx, f, EPS)

    y_range = linspace(0, 1, ny)
    intrgral2 = sympson_integral(y_range, F)
    return intrgral2


if __name__ == '__main__':
    # TEST SPLINE by funcs
    # test_spline()
    ##

    # INTEGRAL PART
    x_vals, y_vals, z_vals = read_data(FILENAME)

    for i in range(len(z_vals)):
        z_vals[i] = list(map(lambda x: log(x), z_vals[i]))

    use_functmp = spline_f_xy_(x_vals, y_vals, z_vals)
    use_func = lambda x, y: exp(use_functmp(x, y))

    intrgral2 = get_integral(use_func, 30, 10)
    ##

    print(f'integral2 = {intrgral2}')

    tab_diff()
