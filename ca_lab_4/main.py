from in_output import choose_act, input_filename, MENU, print_table_data, input_coord, print_table_data_with_err
from work_data import read_data, change_weight, change_weight_to_same, input_change_weight
from approximate import least_squares_method_xy, input_n, least_squares_method_xyz
from graphic import draw_graphic_xy, draw_graphic_xyz, draw_graphic_diffur
from diffur import solve_diffur, solve_original
from Point import *
import copy
import numpy as np

if __name__ == '__main__':
    act = -1
    mode = ''
    data = []
    a_vals = []
    while act != len(MENU) - 1:
        act = choose_act()
        if act == len(MENU) - 1:
            continue
        elif act == 7:
            x_values = np.linspace(0, 1, 10)
            func2, c_values2 = solve_diffur(x_values, 2)
            func3, c_values3 = solve_diffur(x_values, 3)
            print(f'm = {2}, ' + ' '.join([f'C{i}={c_values2[i]}' for i in range(2)]))
            print(f'm = {3}, ' + ' '.join([f'C{i}={c_values3[i]}' for i in range(3)]))
            draw_graphic_diffur(x_values, solve_original, func2, func3)
        elif act == 0 or act == 1:
            a_vals = []
            if act == 0:
                mode = XY
            else:
                mode = XYZ
            filename = input_filename()
            try:
                data = read_data(filename, mode)
                print("Данные успешно прочитаны")
            except Exception as msg:
                print(msg)
                mode = ''
        elif mode != XY and mode != XYZ:
            print('ERROR: Сначала введите данные')
            continue
        elif act == 2:
            print_table_data(data, mode)
        elif act == 3:
            change_weight(data, mode)
        elif act == 4:
            w = input_change_weight()
            change_weight_to_same(data, w)
        elif act == 5 or act == 6:
            n = input_n()
            if mode == XY:
                func = least_squares_method_xy(data, n, printing=True)
                # ERROR
                sum_err = 0
                for p in data:
                    er = p.w * (func(p.x) - p.y) ** 2
                    p.err = er
                    sum_err += er
                print_table_data_with_err(data, mode)
                print(f'SUM ERR = {sum_err:.5f}')
                #
                if act == 6:
                    x = input_coord(mode)
                    y = func(x)
                    print(f'y({x}) = {y:.5f}')
                else:
                    data1 = copy.deepcopy(data)
                    change_weight_to_same(data1, 1)
                    func1 = least_squares_method_xy(data1, n, printing=False)
                    draw_graphic_xy(data, func, func1)
            elif mode == XYZ:
                func = least_squares_method_xyz(data, n, printing=True)
                # ERROR
                sum_err = 0
                for p in data:
                    er = p.w * (func(p.x, p.y) - p.z) ** 2
                    p.err = er
                    sum_err += er
                print_table_data_with_err(data, mode)
                print(f'SUM ERR = {sum_err:.5f}')
                #
                if act == 6:
                    x, y = input_coord(mode)
                    z = func(x, y)
                    print(f'z(x, y) = z({x}, {y}) = {z:.5f}')
                else:
                    draw_graphic_xyz(data, func)
            print(mode)






