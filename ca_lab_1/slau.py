from work_data import read_data_f_g, build_short_data_x_from_data, build_short_data_root_from_data
from newton import polynom_newton
from search_root_newton import search_root_polynom_newton

n = 5


def reverse_f_data(f_data):
    for i in range(len(f_data)):
        f_data[i] = [f_data[i][1], f_data[i][0]]
    return f_data


# return fg_data = [[x, g(x), f(x)], ...]
def expand_g_with_f_data(f_data, g_data, printing=True):
    f_data = reverse_f_data(f_data)
    for i in range(len(g_data)):
        x = g_data[i][0]
        short_data = build_short_data_x_from_data(f_data, x, n + 1)
        fx = polynom_newton(short_data, x, n, printing)
        g_data[i].append(fx)

    if printing:
        print('g_data:')
        for i in range(len(g_data)):
            print(g_data[i])
    return g_data


# return diff_data [[x, f(x) - g(x)], ...]
def build_tab_diff_f_g(fg_data, printing=True):
    diff_data = list()
    for i in range(len(fg_data)):
        diff_data.append([fg_data[i][0], fg_data[i][1] - fg_data[i][2]])

    if printing:
        print('(f - g)(x)')
        for i in range(len(diff_data)):
            print(diff_data[i])
    return diff_data


def solve_slau(file_f, file_g, n, printing=True):
    f_data, g_data = read_data_f_g(file_f, file_g)
    fg_data = expand_g_with_f_data(f_data, g_data, printing)
    diff_data = build_tab_diff_f_g(fg_data, printing)
    diff_data = build_short_data_root_from_data(diff_data, n + 1, printing)
    x_root = search_root_polynom_newton(diff_data, n, printing)

    y_root = polynom_newton(g_data, x_root, n, printing)

    if printing:
        print(f'(f - g)(x) = 0, x = {x_root} => g(x) = {y_root}')
    return x_root, y_root


