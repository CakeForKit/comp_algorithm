from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

from newton import second_derivative_newton_n3, polynom_newton
from spline import spline

DEBUG = True
EPS = 1e-5
STEP_X = 0.05
X_BEG, X_END = 0, 4.2 + STEP_X
# X_BEG, X_END = 3.3, 3.5 + STEP_X
accuracy = 5


def draw_graphic(data, print_tab=False, printing=False):
    # plt.figure(figsize=(8, 8))
    len_data_gt_4 = len(data) >= 4
    newton_data, spline00, spline10, spline11 = list(), list(), list(), list()

    if len_data_gt_4:
        second_derivative_newton_n3_beg = second_derivative_newton_n3(data, data[0][0])
        second_derivative_newton_n3_end = second_derivative_newton_n3(data, data[-1][0])
        # second_derivative_newton_n3_beg = 6 * data[0][0]
        # second_derivative_newton_n3_end = 6 * data[-1][0]
    x_beg, x_end = data[0][0], data[-1][0]
    x_coord = np.arange(x_beg, x_end + STEP_X, STEP_X)
    for x in x_coord:
        i = 0
        while x < data[i][0]:
            i += 1
        if x == data[i][0]:
            y = data[i][1]
            newton_data.append([x, y])
            spline00.append([x, y])
            if len_data_gt_4:
                spline10.append([x, y])
                spline11.append([x, y])
        else:
            y_newton = polynom_newton(data, x, 3)
            y_spline00 = spline(data, x, 0, 0)
            if len_data_gt_4:
                y_spline10 = spline(data, x, second_derivative_newton_n3_beg, 0)
                y_spline11 = spline(data, x, second_derivative_newton_n3_beg, second_derivative_newton_n3_end)

            newton_data.append([x, y_newton])
            spline00.append([x, y_spline00])
            if len_data_gt_4:
                spline10.append([x, y_spline10])
                spline11.append([x, y_spline11])

    # Таблица
    if print_tab and len_data_gt_4:
        tab = PrettyTable()
        tab.field_names = ['x', 'Newton', 'spline00', 'spline10', 'spline11', ]
        for i in range(len(newton_data)):
            tab.add_row([f'{newton_data[i][0]:.{accuracy}f}',
                         f'{newton_data[i][1]:.{accuracy}f}', f'{spline00[i][1]:.{accuracy}f}',
                         f'{spline10[i][1]:.{accuracy}f}', f'{spline11[i][1]:.{accuracy}f}'])
        print(tab)
    #
    y_newton_coord = list(map(lambda xy: xy[1], newton_data))
    y_spline00_coord = list(map(lambda xy: xy[1], spline00))
    plt.plot(x_coord, y_newton_coord, color='r', label='Newton n=3')
    plt.plot(x_coord, y_spline00_coord, color='g', label='Spline beg=0 end=0')
    if len_data_gt_4:
        y_spline10_coord = list(map(lambda xy: xy[1], spline10))
        y_spline11_coord = list(map(lambda xy: xy[1], spline11))
        plt.plot(x_coord, y_spline10_coord, color='b', label='Spline beg=P3''(x0) end=0')
        plt.plot(x_coord, y_spline11_coord, color='m', label='Spline beg=P3''(x0) end=P3''(xn)')

    plt.xlabel('Ось х')  # Подпись для оси х
    plt.ylabel('Ось y')  # Подпись для оси y
    plt.title('График')  # Название
    plt.legend()
    plt.show()


# if __name__ == '__main__':
#     draw_graphic(FILE_DATA, N, printing=DEBUG)