from prettytable import PrettyTable
from Point import *

MENU = [
    "Прочитать из файла таблицу для одномерной аппроксимации",
    "Прочитать из файла таблицу для двумерной аппроксимации",
    "Вывести таблицу",
    "Изменить вес точек",
    "Сделать вес всех точек одинаковым",
    "Решить и построить график",
    "Решить для заданных координат",
    "Приближенное аналитическое решение обыкновенного дифференциального уравнения",
    "Выход"
]
CHOOSE_ACT = "Выберите номер действия: "
INPUT_FILE = "Введите название файла: "


def print_menu():
    print()
    for i, val in enumerate(MENU):
        print(f'{i}: {val}')


def choose_act():
    act = -1

    print_menu()
    while act < 0 or act >= len(MENU):
        print(CHOOSE_ACT, end='')
        try:
            act = int(input())
            if not (0 <= act < len(MENU)):
                raise Exception
        except Exception:
            print("ERROR: неверный номер действия, попробуйте снова")
            act = -1
    return act


def input_filename():
    filename = ''
    while filename == '':
        print(INPUT_FILE, end='')
        filename = input()
        if filename in ['41', '42', '43', '44']:
            filename = 'data/tmp' + filename
        try:
            f = open(filename, 'r')
            f.close()
        except Exception:
            print(f"ERROR: ошибка открытия файла '{filename}', попробуйте снова")
            filename = ''
    return filename


def print_table_data(data: list[Point], mode):
    tab = PrettyTable()
    if mode == XY:
        tab.field_names = ['x', 'y', 'weight']
        for i in range(len(data)):
            p = data[i]
            tab.add_row([p.x, p.y, p.w])
        print(tab)
    else:
        tab.field_names = ['z', 'x', 'y', 'weight']
        for i in range(len(data)):
            p = data[i]
            tab.add_row([p.z, p.x, p.y, p.w])
        print(tab)


def print_slau(slau):
    width = 20
    accur = 2

    row = ' '.join(list(map(lambda i: f'a{i}', range(len(slau)))))
    print(f'SLAU: ({row})')
    for i in range(len(slau)):
        row = ''.join(list(map(lambda x: f'{x:{width}.{accur}f}', slau[i])))
        print(row)


def input_coord(mode):
    x, y = None, None
    if mode == XY:
        good = False
        while not good:
            print('Введите x: ', end='')
            try:
                x = float(input())
                good = True
            except Exception:
                print('ERROR: введите float')
        return x
    else:
        good = False
        while not good:
            print('Введите (x, y): ', end='')
            try:
                x, y = map(float, input().split())
                good = True
            except Exception:
                print('ERROR: введите float float')
        return x, y


def print_table_data_with_err(data: list[Point], mode):
    tab = PrettyTable()
    if mode == XY:
        tab.field_names = ['x', 'y', 'weight', 'err']
        for i in range(len(data)):
            p = data[i]
            tab.add_row([p.x, f'{p.y:.5f}', p.w, f'{p.err:.5f}'])
        print(tab)
    else:
        tab.field_names = ['z', 'x', 'y', 'weight', 'err']
        for i in range(len(data)):
            p = data[i]
            tab.add_row([p.z, p.x, f'{p.y:.5f}', p.w, f'{p.err:.5f}'])
        print(tab)
