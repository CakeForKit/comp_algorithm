from prettytable import PrettyTable
from numpy import linspace, log

FILENAME = 'data/table_for_diff.txt'
ONE_SIZE_DIFF = 'one_side_diff'
MID_DIFF = 'mid_diff'
RUNGE = 'runge_diff'
LEVELING = 'leveling_diff'
DIFF2 = 'diff 2'


def read_table_for_diff(file_name=FILENAME):
    data = dict()
    data['x'] = []
    data['y'] = []

    with open(file_name) as file:
        line = file.readline()
        while line != '':
            x, y = map(float, line.split())
            data['x'].append(x)
            data['y'].append(y)
            line = file.readline()
    return data


def one_side_diff(x, y):
    return [(y[i + 1] - y[i]) / (x[i + 1] - x[i]) for i in range(len(x) - 1)] + \
        [(y[-3] - 4 * y[-2] + 3 * y[-1]) / (x[-1] - x[-3])]


def mid_diff(x, y):
    return [(-3 * y[0] + 4 * y[1] - y[2]) / (x[2] - x[0])] + \
        [(y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1]) for i in range(1, len(x) - 1)] + \
        [(y[-3] - 4 * y[-2] + 3 * y[-1]) / (x[-1] - x[-3])]


def runge(x, y):
    m = 2
    res = []
    for i in range(len(x) - 2):
        Zxh = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        Zxkh = (y[i + 2] - y[i]) / (x[i + 2] - x[i])
        u = Zxh + (Zxh - Zxkh) / (m - 1)

        res.append(u)
    res.append((y[-4] - 4 * y[-3] + 3 * y[-2]) / (x[-1] - x[-4]))
    res.append((y[-3] - 4 * y[-2] + 3 * y[-1]) / (x[-1] - x[-3]))
    return res


def leveling_diff(x, y):
    def level(x):
        return log(x)

    xl = list(map(level, x))
    yl = list(map(level, y))

    res = [(-3 * y[0] + 4 * y[1] - y[2]) / (x[2] - x[0])]
    for i in range(1, len(x) - 1):
        yd = (yl[i + 1] - yl[i]) / (xl[i + 1] - xl[i]) * y[i] / x[i]
        res.append(yd)
    res.append((y[-3] - 4 * y[-2] + 3 * y[-1]) / (x[-1] - x[-3]))
    return res


def diff2(x, y):
    # [(y[2] - 2 * y[1] + y[0]) / ((x[2] - x[1]) * (x[1] - x[0]))]
    return [(-y[3] + 4 * y[2] - 5 * y[1] + 2 * y[0]) / ((x[1] - x[0]) ** 2)] + \
        [(y[i - 1] - 2 * y[i] + y[i + 1]) / ((x[i + 1] - x[i]) ** 2) for i in range(1, len(x) - 1)] + \
        [(-y[-4] + 4 * y[-3] - 5 * y[-2] + 2 * y[-1]) / ((x[-2] - x[-1]) ** 2)]
    # [(y[-3] - 2 * y[-2] + y[-1]) / ((x[-3] - x[-2]) * (x[-2] - x[-1]))]


# data = dict('x': list, 'y': list)
def count_tab_diff(data):
    data[ONE_SIZE_DIFF] = one_side_diff(data['x'], data['y'])
    data[MID_DIFF] = mid_diff(data['x'], data['y'])
    data[RUNGE] = runge(data['x'], data['y'])
    data[LEVELING] = leveling_diff(data['x'], data['y'])
    data[DIFF2] = diff2(data['x'], data['y'])
    return data


def print_tab_diff(data):
    tab = PrettyTable()

    tab.field_names = list(data.keys())
    for i in range(len(data['x'])):
        tab.add_row([f'{data[k][i]:.3f}' for k in data.keys()])

    # tab.add_row(['-', '-', 'O(h)', 'O(h^2)', 'O(h^2)', '-'])
    print(tab)


def tab_diff(filename=FILENAME):
    data = read_table_for_diff(filename)
    data = count_tab_diff(data)
    print_tab_diff(data)


def test():
    def func(x):
        return x ** 3.2

    def dfunc(x):
        return 3.2 * x ** 2.2

    def ddfunc(x):
        return 3.2 * 2.2 * x ** 1.2

    x = list(linspace(0.1, 2.8, 10))
    y = [func(xi) for xi in x]
    data = dict()
    data['x'] = x
    data['y'] = y

    data = count_tab_diff(data)
    data['real'] = [dfunc(xi) for xi in x]
    data['real2'] = [ddfunc(xi) for xi in x]
    print_tab_diff(data)


if __name__ == '__main__':
    test()
