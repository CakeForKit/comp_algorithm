from MatrixF_ZYX import MatrixF_ZYX
from spline_Matrix import spline_zi_yi_fx, spline_zi_fxy
from newton_Matrix import newton_zi_yi_fx, newton_zi_fxy
from spline import spline
from newton import polynom_newton_from_short_data


# x - newton, y - spline
def nn_zi_fxy(matrixf_xy, x, y, nx, ny):
    return newton_zi_fxy(matrixf_xy, x, y, nx, ny)


def ns_zi_fxy(matrixf_xy, x, y, ny):
    nearest_val_ind = matrixf_xy.get_nearest_y(y, ny + 1)
    data_fy = []  # [(y, f), ...]
    for val, ind in nearest_val_ind:
        f = spline_zi_yi_fx(matrixf_xy, ind, x)
        data_fy.append([val, f])
    polynom_fy = polynom_newton_from_short_data(data_fy, y, ny)
    return polynom_fy


def sn_zi_fxy(matrixf_xy, x, y, nx):
    data_fy = []  # [(y, f), ...]
    for ind, val in enumerate(matrixf_xy.y):
        f = newton_zi_yi_fx(matrixf_xy, ind, x, nx)
        data_fy.append([val, f])
    spline_fy = spline(data_fy, y)
    return spline_fy


def ss_zi_fxy(matrixf_xy, x, y):
    return spline_zi_fxy(matrixf_xy, x, y)


def nns_mixed_fxyz(matrix: MatrixF_ZYX, x, y, z, nx, ny):
    data_fz = []  # [(y, f), ...]
    for val, ind in enumerate(matrix.z):
        f = nn_zi_fxy(matrix.f_XOY[ind], x, y, nx, ny)
        data_fz.append([val, f])

    spline_fz = spline(data_fz, z)
    return spline_fz


def nsn_mixed_fxyz(matrix: MatrixF_ZYX, x, y, z, ny, nz):
    nearest_val_ind = matrix.get_nearest_z(z, nz + 1)
    data_fz = []  # [(y, f), ...]
    for val, ind in nearest_val_ind:
        f = ns_zi_fxy(matrix.f_XOY[ind], x, y, ny)
        data_fz.append([val, f])

    polynom_fz = polynom_newton_from_short_data(data_fz, z, nz)
    return polynom_fz


def nss_mixed_fxyz(matrix: MatrixF_ZYX, x, y, z, ny):
    data_fz = []  # [(y, f), ...]
    for val, ind in enumerate(matrix.z):
        f = ns_zi_fxy(matrix.f_XOY[ind], x, y, ny)
        data_fz.append([val, f])

    # print_data_tab(data_fz, 'x', 'f')
    spline_fz = spline(data_fz, z)
    return spline_fz


def snn_mixed_fxyz(matrix: MatrixF_ZYX, x, y, z, nx, nz):
    nearest_val_ind = matrix.get_nearest_z(z, nz + 1)
    data_fz = []  # [(y, f), ...]
    for val, ind in nearest_val_ind:
        f = sn_zi_fxy(matrix.f_XOY[ind], x, y, nx)
        data_fz.append([val, f])

    polynom_fz = polynom_newton_from_short_data(data_fz, z, nz)
    return polynom_fz


def sns_mixed_fxyz(matrix: MatrixF_ZYX, x, y, z, nx):
    data_fz = []  # [(y, f), ...]
    for val, ind in enumerate(matrix.z):
        f = sn_zi_fxy(matrix.f_XOY[ind], x, y, nx)
        data_fz.append([val, f])

    # print_data_tab(data_fz, 'x', 'f')
    spline_fz = spline(data_fz, z)
    return spline_fz


def ssn_mixed_fxyz(matrix: MatrixF_ZYX, x, y, z, nz):
    nearest_val_ind = matrix.get_nearest_z(z, nz + 1)
    data_fz = []  # [(y, f), ...]
    for val, ind in nearest_val_ind:
        f = ss_zi_fxy(matrix.f_XOY[ind], x, y)
        data_fz.append([val, f])

    polynom_fz = polynom_newton_from_short_data(data_fz, z, nz)
    return polynom_fz
