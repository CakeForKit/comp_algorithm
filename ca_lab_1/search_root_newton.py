from prettytable import PrettyTable
from work_data import read_data_search_root
from newton import sep_diff_newton, count_polynom_newton


def print_reversed_tab_sep_diff_newton(data):
    tab = PrettyTable()
    tab.field_names = ['y', 'x'] + list(map(lambda x: f'Y{x}', range(1, len(data[0]) - 1)))
    for i in range(len(data)):
        row_list = list(map(lambda x: float(f'{x:.5f}'), data[i]))
        row_list += (len(data[0]) - len(data[i])) * ['-']
        tab.add_row(row_list)
    print(tab)


def build_reversed_tab_sep_diff_newton(data):
    tab = list()
    for i in range(len(data)):
        tab.append([data[i][1], data[i][0]])
    sep_diff_newton(tab, 0, len(tab) - 1)
    return tab


# data = [[x, y], ...]
def search_root_polynom_newton(data, n, printing=True):
    x = 0
    tab = build_reversed_tab_sep_diff_newton(data)
    if printing:
        print('Поиск корня (полином Ньютона)')
        print_reversed_tab_sep_diff_newton(tab)

    polynom = count_polynom_newton(tab, x)
    if printing:
        print(f'P{n}({x}) = {polynom:.5f}')
    return polynom


def search_root_newton(file_data, n, printing=True):
    x = 0
    data = read_data_search_root(file_data, n)
    if len(data) > 0:
        p = search_root_polynom_newton(data, n, printing)

        if printing:
            print(f'x(y = 0) = {p}')
    return p

