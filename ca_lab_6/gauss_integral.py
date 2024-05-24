from math import cos, pi
from gauss import gauss

pascal_triangle_data = [[1]]


def get_pascal_trisngle(n):
    for i in range(len(pascal_triangle_data), n + 1):
        row = [1]
        for k in range(len(pascal_triangle_data[i - 1]) - 1):
            row.append(pascal_triangle_data[i - 1][k] + pascal_triangle_data[i - 1][k + 1])
        row.append(1)
        pascal_triangle_data.append(row)


def pascal_triangele(n, k):
    get_pascal_trisngle(n)
    # print(len(pascal_triangle_data), len(pascal_triangle_data[n]), n, k)
    return pascal_triangle_data[n][k]


def legandre_polymon_bin_coeff(n, x):
    summ = 0
    for k in range(n // 2 + 1):
        elem = (-1) ** k
        nk = pascal_triangele(n, k)
        n2_k2_n = pascal_triangele(2 * n - 2 * k, n)
        elem *= nk * n2_k2_n * x ** (n - 2 * k)
        summ += elem
    return 1 / 2 ** n * summ


def legandre_polymon_recursion(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return (2 * n - 1) / n * x * legandre_polymon_recursion(n - 1, x) - (n - 1) / n * legandre_polymon_recursion(
            n - 2, x)


def legandre_polymon(n, x):
    return legandre_polymon_bin_coeff(n, x)


def legandre_1derivative(n, x):
    return n / (1 - x ** 2) * (legandre_polymon(n - 1, x) - x * legandre_polymon(n, x))


# n - count_roots
def legandre_roots(n, eps):
    roots = list()
    for i in range(n):
        x0 = cos(pi * (4 * i + 3) / (4 * n + 2))
        roots.append(x0)

        pnk = legandre_polymon(n, x0)
        while abs(pnk) > eps:
            xk = roots[i]
            dpnk = legandre_1derivative(n, xk)
            roots[i] = xk - pnk / dpnk
            pnk = legandre_polymon(n, roots[i])
    return roots


def gauss_integral(a, b, n, func, eps):
    t_vals = legandre_roots(n, eps)
    x_vals = [(b + a) / 2 + (b - a) / 2 * ti for ti in t_vals]

    slauA = [[t_vals[j] ** i for j in range(n)] for i in range(n)]
    integral_tk = [2 / (i + 1) if i % 2 == 0 else 0 for i in range(n)]
    slauA = [slauA[i] + [integral_tk[i]] for i in range(n)]

    coeff_A = gauss(slauA, False)
    return (b - a) / 2 * sum([coeff_A[i] * func(x_vals[i]) for i in range(n)])
