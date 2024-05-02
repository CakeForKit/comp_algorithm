from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

from work_data import read_data, read_short_data
from newton import polynom_newton
from hermit import polynom_hermit

DEBUG = True
EPS = 1e-5
FILE_DATA = 'data.txt'
N = 2
STEP_X = 0.1
X_BEG, X_END = 0, 4.2 + STEP_X
# X_BEG, X_END = 3.3, 3.5 + STEP_X
accuracy = 5


def draw_graphic(file_data, n, printing=True):
    plt.figure(figsize=(8, 8))
    data = read_data(file_data)
    newton_data, hermit_data = list(), list()

    x_coord = np.arange(X_BEG, X_END, STEP_X)
    for x in x_coord:
        i = 0
        while x < data[i][0]:
            i += 1
        if x == data[i][0]:
            y = data[i][1]
            newton_data.append([x, y])
            hermit_data.append([x, y])
        else:
            short_data = read_short_data(file_data, x, n)
            p = polynom_newton(short_data, x, n, printing=True)
            # h = polynom_hermit(short_data, x, n, printing)

            newton_data.append([x, p])
            hermit_data.append([x, p])

    # Таблица
    tab = PrettyTable()
    tab.field_names = ['x', 'Newton', 'Hermit', 'diff']
    for i in range(len(newton_data)):
        tab.add_row([f'{newton_data[i][0]:.{accuracy}f}',
                     f'{newton_data[i][1]:.{accuracy}f}', f'{hermit_data[i][1]:.{accuracy}f}',
                     f'{newton_data[i][1] - hermit_data[i][1]:.{accuracy}f}'])
    print(f'n = {n}')
    print(tab)
    #
    y_newton_coord = list(map(lambda xy: xy[1], newton_data))
    y_hermit_coord = list(map(lambda xy: xy[1], hermit_data))
    plt.plot(x_coord, y_newton_coord, color='r', label='Newton')
    plt.plot(x_coord, y_hermit_coord, color='b', label='Hermit')

    plt.xlabel('Ось х')  # Подпись для оси х
    plt.ylabel('Ось y')  # Подпись для оси y
    plt.title('График')  # Название
    plt.show()


if __name__ == '__main__':
    draw_graphic(FILE_DATA, N, printing=DEBUG)