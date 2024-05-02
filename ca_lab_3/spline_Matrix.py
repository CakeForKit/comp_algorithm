from MatrixF_ZYX import MatrixF_ZYX
from spline import spline
from prettytable import PrettyTable


def print_data_tab(data, s1, s2):
    tab = PrettyTable()
    tab.field_names = [s1, s2]
    for i in range(len(data)):
        row_list = list(map(str, data[i]))
        tab.add_row(row_list)
    print(tab)


def spline_zi_yi_fx(matrixf_xy, index_yi, x):
    data_fx = list(zip(matrixf_xy.x, matrixf_xy.f[index_yi]))
    spline_fx = spline(data_fx, x)
    return spline_fx


def spline_zi_fxy(matrixf_xy, x, y):
    data_fy = []  # [(y, f), ...]
    for ind, val in enumerate(matrixf_xy.y):
        f = spline_zi_yi_fx(matrixf_xy, ind, x)
        data_fy.append([val, f])
    spline_fy = spline(data_fy, y)
    return spline_fy


def spline_fxyz(matrix: MatrixF_ZYX, x, y, z):
    data_fz = []  # [(y, f), ...]
    # print(matrix.z)
    for ind, val in enumerate(matrix.z):
        f = spline_zi_fxy(matrix.f_XOY[ind], x, y)
        data_fz.append([val, f])

    # print_data_tab(data_fz, 'x', 'f')
    spline_fz = spline(data_fz, z)
    return spline_fz


def tmp_test_cmp_file(fhe, fmy):
    eps = 1e-5
    with open(fhe, 'r') as he_file:
        with open(fmy, 'r') as my_file:
            he = he_file.readline().split()
            my = my_file.readline().split()
            while he != [] and my != []:
                if float(he[4]) != float(my[4]):
                    print(*he, '-', *my, '\t', f'{abs(float(he[4]) - float(my[4])):.5f}')
                he = he_file.readline().split()
                my = my_file.readline().split()


if __name__ == '__main__':
    matrix_F_XYZ = MatrixF_ZYX('data.txt')
    x, y, z = 1.3, 1.05, 0.82
    fxyz = spline_fxyz(matrix_F_XYZ, x, y, z)
    print(fxyz)

    with open('cmp_file_my.txt', 'w') as file:
        matrix_F_XYZ = MatrixF_ZYX('data.txt')
        step = 0.5
        x, y, z = 0, 0, 0
        while z <= 4:
            y = 0
            while y <= 4:
                x = 0
                while x <= 4:
                    fxyz = spline_fxyz(matrix_F_XYZ, x, y, z)
                    file.write(f'{x:.2f} {y:.2f} {z:.2f} - {fxyz}\n')
                    x += step
                y += step
            z += step

    tmp_test_cmp_file('cmp_file_ratwe.txt', 'cmp_file_my.txt')
