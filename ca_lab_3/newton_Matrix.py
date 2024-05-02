from MatrixF_ZYX import MatrixF_ZYX
from newton import polynom_newton_from_short_data
from prettytable import PrettyTable


def print_data_tab(data, s1, s2):
    tab = PrettyTable()
    tab.field_names = [s1, s2]
    for i in range(len(data)):
        row_list = list(map(str, data[i]))
        tab.add_row(row_list)
    print(tab)

def newton_zi_yi_fx(matrixf_xy, index_yi, x, nx):
    data_fx = matrixf_xy.get_data_nearest_x_for_yi(index_yi, x, nx)
    polynom_fx = polynom_newton_from_short_data(data_fx, x, nx)
    return polynom_fx


def newton_zi_fxy(matrixf_xy, x, y, nx, ny):
    nearest_val_ind = matrixf_xy.get_nearest_y(y, ny + 1)
    data_fy = [] # [(y, f), ...]
    for val, ind in nearest_val_ind:
        f = newton_zi_yi_fx(matrixf_xy, ind, x, nx)
        data_fy.append([val, f])
    polynom_fy = polynom_newton_from_short_data(data_fy, y, ny)
    return polynom_fy


def newton_fxyz(matrix: MatrixF_ZYX, x, y, z, nx, ny, nz):
    nearest_val_ind = matrix.get_nearest_z(z, nz + 1)
    data_fz = []  # [(y, f), ...]
    for val, ind in nearest_val_ind:
        f = newton_zi_fxy(matrix.f_XOY[ind], x, y, nx, ny)
        data_fz.append([val, f])

    # print_data_tab(data_fz, 'x', 'f')

    polynom_fz = polynom_newton_from_short_data(data_fz, z, nz)
    return polynom_fz


def tmp_test_cmp_file(fhe, fmy):
    eps = 1e-5
    with open(fhe, 'r') as he_file:
        with open(fmy, 'r') as my_file:
            he = he_file.readline().split()
            my = my_file.readline().split()
            while he != [] and my != []:
                if float(he[4]) != float(my[4]):
                    print(*he, '-', *my)
                he = he_file.readline().split()
                my = my_file.readline().split()



if __name__ == '__main__':
    matrix_F_XYZ = MatrixF_ZYX('data.txt')
    x, y, z = 1.3, 1.05, 0.82
    nx, ny, nz = 2, 2, 2
    polynom = newton_fxyz(matrix_F_XYZ, x, y, z, nx, ny, nz)
    print(polynom)


    with open('cmp_file_my.txt', 'w') as file:
        matrix_F_XYZ = MatrixF_ZYX('data.txt')
        nx, ny, nz = 3, 3, 3
        step = 0.5
        x, y, z = 0, 0, 0
        while z <= 5:
            y = 0
            while y <= 5:
                x = 0
                while x <= 5:
                    polynom = newton_fxyz(matrix_F_XYZ, x, y, z, nx, ny, nz)
                    file.write(f'{x:.2f} {y:.2f} {z:.2f} - {polynom}\n')
                    x += step
                y += step
            z += step

    tmp_test_cmp_file('cmp_file_ratwe.txt', 'cmp_file_my.txt')
