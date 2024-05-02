from prettytable import PrettyTable


def sort_data(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]


def read_data(filename):
    data = list()
    with open(filename) as f:
        line = f.readline()
        while line != '':
            data.append(list(map(float, line.split())))
            line = f.readline()
    sort_data(data)
    return data


def print_data(data):
    tab = PrettyTable()
    tab.field_names = ['x', 'y']
    for i in range(len(data)):
        tab.add_row(data[i])
    print(tab)
