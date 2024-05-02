from Point import *


class ErrorData(Exception):
    pass


# return [Point, ...]
def read_data(filename, mode) -> list[Point]:
    data = []
    with open(filename, 'r') as file:
        file.readline()
        line = file.readline()
        while line != '':
            line = list(map(float, line.split()))
            if mode == XY:
                if len(line) != 3:
                    raise ErrorData("Неверное количество столбцов")
                x, y, w = line
                data.append(Point(w, x, y))
            else:
                if len(line) != 4:
                    raise ErrorData("Неверное количество столбцов")
                z, x, y, w = line
                data.append(Point(w, x, y, z))
            line = file.readline()
    return data


def change_weight(data, mode):
    print('Изменяем вес каждой точки в таблице (нажмите enter чтобы оставить вес предыдущим)')
    if mode == XY:
        print('Point(x, y, weight)')
    else:
        print('Point(z, x, y, weight)')
    for i in range(len(data)):
        good = False
        while not good:
            print(f'Point{data[i]}: ', end='')
            new = input()
            if new == '':
                good = True
                new = data[i].w
            else:
                try:
                    new = float(new)
                    good = True
                except Exception:
                    print('ERROR: такого веса быть не может, попробуйте снова')
        data[i].w = new


def input_change_weight():
    print('Введите вес, который хотите чтобы был у всех точек: ', end='')
    good = False
    while not good:
        try:
            w = float(input())
            good = True
        except Exception:
            print('ERROR: такого веса быть не может, попробуйте снова')
    return w

def change_weight_to_same(data, w):
    for i in range(len(data)):
        data[i].w = w