from Point import *
from in_output import print_slau
from gauss import gauss
import  math as m

def input_n():
    good = False
    while not good:
        print('Введите степень аппроксимирующего полинома: ', end='')
        try:
            n = int(input())
            good = True
        except Exception:
            print('ERROR введите целое число > 0')
    return n


def get_slau_xy(data, n):
    slau = []

    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            row.append(sum(list(map(
                lambda p: (p.x ** (i + j)) * p.w, data))))
        row.append(sum(list(map(
            lambda p: (p.x ** i) * p.y * p.w, data))))
        slau.append(row)
    return slau


def least_squares_method_xy(data, n, printing=True):  # -> a_values
    slau = get_slau_xy(data, n)
    if printing:
        print_slau(slau)
    a_values = gauss(slau, printing)
    if printing:
        for i in range(len(a_values)):
            print(f'a{i} = {a_values[i]:.5f}')
    print()

    # print('ERROR=')
    # for p in data:


    def f(x):
        res = 0
        for i in range(len(a_values)):
            res += a_values[i] * x ** i
        return res
    return f


def get_slau_xyz(data, n):
    slau = []

    for i in range(n + 1):
        for j in range(n + 1 - i):
            row = []
            for k in range(n + 1):
                for u in range(n + 1 - k):
                    row.append(sum(list(map(
                        lambda p: (p.x ** (k + i)) * (p.y ** (u + j)) * p.w, data))))

            row.append(sum(list(map(
                lambda p: (p.x ** i) * (p.y ** j) * p.z * p.w, data))))
            slau.append(row)
    return slau


def least_squares_method_xyz(data, n, printing=True):  # -> a_values
    # Change t = exp(y)
    for p in data:
        p.y = m.exp(p.y)


    slau = get_slau_xyz(data, n)
    if printing:
        print_slau(slau)
    a_values = gauss(slau, printing)
    if printing:
        for i in range(len(a_values)):
            print(f'a{i} = {a_values[i]:.5f}')
    print()

    def f(x, y):
        res = 0
        ind = 0
        for i in range(n + 1):
            for j in range(n + 1 - i):
                res += a_values[ind] * (x ** i) * (y ** j)
                ind += 1
        return res
    return f
