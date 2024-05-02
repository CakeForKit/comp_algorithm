from prettytable import PrettyTable
from work_data import read_data_search_root
from plus_cod import find_root

def print_reversed_tab_sep_diff_hermit(data):
    tab = PrettyTable()
    tab.field_names = ['y', 'x', "x'", "x''"] + list(map(lambda x: f'Y{x}', range(1, len(data[0]) - 3)))
    for i in range(len(data)):
        row_list = list(map(lambda x: float(f'{x:.5f}'), data[i]))
        row_list += (len(data[0]) - len(data[i])) * ['-']
        tab.add_row(row_list)
    print(tab)


# tab - таблица для разделенных разностей n порядка
def sep_diff_hermit(tab, begi, endi):
    diff = endi - begi
    if len(tab[begi]) > diff + 3:
        return tab[begi][diff + 3]

    if diff == 1 and begi // 3 == endi // 3:
        y = tab[begi][2]
    elif diff == 2 and begi // 3 == endi // 3:
        sep_diff_hermit(tab, begi, endi - 1)
        sep_diff_hermit(tab, begi + 1, endi)
        # print_tab_sep_diff_hermit(tab)
        y = tab[begi][3] / 2
    elif diff == 1:
        y = (tab[begi][1] - tab[endi][1]) / (tab[begi][0] - tab[endi][0])
    else:
        y = (sep_diff_hermit(tab, begi, endi - 1) - sep_diff_hermit(tab, begi + 1, endi)) / (tab[begi][0] - tab[endi][0])
    # print(f'begi, endi = {begi, endi} -> y = {y}')
    tab[begi].append(y)
    return y


def build_reversed_tab_sep_diff_n_hermit(data):
    tab = list()
    try:
        for i in range(len(data)):
            for _ in range(3):
                tab.append([data[i][1], data[i][0], 1 / data[i][2], data[i][3] / (data[i][2] ** 3)])
        sep_diff_hermit(tab, 0, len(tab) - 1)
    except ZeroDivisionError:
        tab = []
        # pass
    return tab


def count_polynom_hermit(tab, x):
    polynom = tab[0][1]
    for i in range(4, len(tab[0])):
        part = tab[0][i]
        # print(f'{part} * ', end='')
        for i in range(i - 3):
            part *= x - tab[i][0]
            # print(f'(x - {tab[i][0]})', )
        polynom += part
    return polynom


def search_root_polynom_hermit(data, n, printing=True):
    x = 0
    tab = build_reversed_tab_sep_diff_n_hermit(data)
    if len(tab) != 0:
        if printing:
            print('Поиск корня (полином Эрмита)')
            print_reversed_tab_sep_diff_hermit(tab)

        polynom = count_polynom_hermit(tab, x)
    else:
        data = [line[:2] for line in data]
        polynom = find_root(data)

    if printing:
        print(f'H{n}({x}) = {polynom:.5f}')
    return polynom


def search_root_hermit(file_data, n, printing=True):
    x = 0
    data = read_data_search_root(file_data, n)
    if len(data) > 0:
        p = search_root_polynom_hermit(data, n, printing)

        if printing:
            print(f'x(y = 0) = {p}')

    return p