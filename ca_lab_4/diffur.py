import numpy as np
from scipy.special import erfi
from gauss import gauss

from in_output import print_slau


class ErrorParam(Exception):
    pass


def solve_original(x):
    return ((-(np.exp(0.5) + 1) / erfi(1 / np.sqrt(2))) * erfi(x / np.sqrt(2)) + 1) / np.exp(x ** 2 / 2) + x


def u0(x):
    return 1 - x


def u1(x):
    return x * (1 - x)


def u2(x):
    return x ** 2 * (1 - x)


def u3(x):
    return x ** 3 * (1 - x)


def c0(x):
    return 1 - 4 * x


def c1(x):
    return - 2 + 2 * x - 3 * x ** 2


def c2(x):
    return 2 - 6 * x + 3 * x ** 2 - 4 * x ** 3


def c3(x):
    return 6 * x - 12 * x ** 2 + 4 * x ** 3 - 5 * x ** 4


def get_slau_diffur(x_values, koeff_func_c):
    slau = []

    # print(' '.join(map(lambda x: str(koeff_func_c[0](x)), x_values[:10])))
    for k_line in koeff_func_c[1:]:
        row = []
        for k_row in koeff_func_c[1:]:
            row.append(sum([k_line(x) * k_row(x) for x in x_values]))
        row.append(-sum([koeff_func_c[0](x) * k_line(x) for x in x_values]))
        slau.append(row)
    return slau


def least_squares_method_diffur(x_values, koeff_func_c, u, printing=False):
    if len(koeff_func_c) != len(u):
        raise ErrorParam('ErrorParam')
    slau = get_slau_diffur(x_values, koeff_func_c)
    if printing:
        print_slau(slau)
    c_values = gauss(slau, printing)
    if printing:
        for i in range(len(c_values)):
            print(f'C{i} = {c_values[i]:.5f}')

    m = len(koeff_func_c)

    def f(x):
        # print(f'mmmmm = {m}')
        # print(c_values)
        return u[0](x) + sum([c_values[i] * u[i + 1](x) for i in range(m - 1)])

    return f, c_values


def solve_diffur(x_values, m):
    if m == 2:
        func, c_values = least_squares_method_diffur(x_values, [c0, c1, c2], [u0, u1, u2])
        return func, c_values
    if m == 3:
        func, c_values = least_squares_method_diffur(x_values, [c0, c1, c2, c3], [u0, u1, u2, u3])
        return func, c_values
    raise ErrorParam('ErrorParam')