from prettytable import PrettyTable
from Point import *


def print_slau(slau):
    width = 20
    accur = 2

    row = ' '.join(list(map(lambda i: f'a{i}', range(len(slau)))))
    print(f'SLAU: ({row})')
    for i in range(len(slau)):
        row = ''.join(list(map(lambda x: f'{x:{width}.{accur}f}', slau[i])))
        print(row)
