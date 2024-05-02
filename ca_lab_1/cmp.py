from prettytable import PrettyTable

from work_data import read_short_data
from newton import polynom_newton
from hermit import polynom_hermit


def build_cmp_table(file_data, x, printing=True):
    tab = PrettyTable()
    tab.field_names = ['n', 'Newton', 'Hermit']
    for n in range(1, 5 + 1):
        data = read_short_data(file_data, x, n)
        p = polynom_newton(data, x, n, printing)
        # h = polynom_hermit(data, x, n, printing)
        h = 0
        tab.add_row([n, f'{p:.5f}', f'{h:.5f}'])
    print()
    print(f'x = {x}')
    print('Таблица сравнения:')
    print(tab)
