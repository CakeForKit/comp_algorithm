from in_output import *
from spline import spline
from newton import second_derivative_newton_n3, polynom_newton
from draw_graphic import draw_graphic

FILENAME = 'data/data.txt'


def main():
    data = read_data(FILENAME)
    if len(data) <= 1:
        print('ERROR: недостаточно данных')
        return
    print_data(data)

    # def f(x):
    #     return x ** 3 - x - 1
    x = float(input('Введите x: '))
    # if x < data[0][0] or x > data[-1][0]:
    #     print('ERROR: x должен быть между макс и мин значениями х в таблице')
    #     return
    # print(f'F({x} = {f(x)}')
    newton = polynom_newton(data, x, 3)
    print(f"Полином Ньютона 3й степени: {newton}")
    spline00 = spline(data, x, 0, 0)
    print(f"Сплайн y''(x0) = 0\t\t\ty'f'(xn) = 0: \t\t{spline00}")

    if len(data) >= 4:
        beg = second_derivative_newton_n3(data, data[0][0])
        end = second_derivative_newton_n3(data, data[-1][0])
    # beg = 6 * data[0][0]
    # end = 6 * data[-1][0]
    # print(f'beg, end = {beg}, {end}')
    spline10 = spline(data, x, beg, 0)
    print(f"Сплайн y''(x0) = P3''(x0)\ty'f'(xn) = 0: \t\t{spline10}")
    spline11 = spline(data, x, beg, end)
    print(f"Сплайн y''(x0) = P3''(x0)\ty''(xn) = P3''(xn): {spline11}")

    draw_graphic(data)

    # x = 0
    # with open('out.txt', 'w') as f:
    #     f.write(f'{beg} - {end}\n')
    #     while x <= 7:
    #         y = spline(data, x, beg, end)
    #
    #         f.write(f'{y}\n')
    #         x += 0.05
    #
    # # CMP
    # with open('out.txt', 'r') as f1:
    #     with open('out1.txt', 'r') as f2:
    #         f1.readline(), f2.readline()
    #         str1, str2 = f1.readline(), f2.readline()
    #         while str1 != '':
    #             my = float(str1)
    #             he = float(str2)
    #             print(f'{abs(my - he):.20f}')
    #             str1, str2 = f1.readline(), f2.readline()


main()
