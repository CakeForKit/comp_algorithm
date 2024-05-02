from cmp import build_cmp_table
from search_root_newton import search_root_newton
from search_root_hermitpy import search_root_hermit
from slau import solve_slau
from draw_graphic import draw_graphic

DEBUG = False

file_data = 'test_data.txt'
file_f, file_g = 'data_f.txt', 'data_g.txt'
accuracy = 5


if __name__ == '__main__':
    x = 0.54
    build_cmp_table(file_data, x, printing=DEBUG)
    # np, nh = 5, 4
    # p = search_root_newton(file_data, np, printing=DEBUG)
    # h = search_root_hermit(file_data, nh, printing=DEBUG)
    # print('\nСравнение вычисления корня:')
    # print(f'полиномом Ньютона (n = {np}):\t{p:.{accuracy}f}')
    # print(f'полиномом Эрмита (n = {nh}):\t{h:.{accuracy}f}')
    #
    # x_root, y_root = solve_slau(file_f, file_g, np, printing=DEBUG)
    # print(f'Решение слау (n = {np}): (x, y) = ({x_root:.{accuracy}f}, {y_root:.{accuracy}f})')

    n = 3
    draw_graphic(file_data, n, printing=DEBUG)


