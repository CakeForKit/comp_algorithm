from MatrixF_ZYX import MatrixF_ZYX
from newton_Matrix import newton_fxyz
from spline_Matrix import spline_fxyz
import numpy as np


def f(x, y, z):
    # return x * y * z
    # return x ** 2 + y ** 2 - z ** 3
    return np.exp(2 * x - y) * z


def test():
    xb, xe, nx = -5, 5, 20
    yb, ye, ny = -3, 4, 50
    zb, ze, nz = -1, 2, 30

    x = list(np.linspace(xb, xe, nx))
    y = list(np.linspace(yb, ye, ny))
    z = list(np.linspace(zb, ze, nz))
    # print(f'z={z}')

    fxy = dict()
    for zz in z:
        fxy[zz] = dict()
        fxy[zz]['x'] = x
        fxy[zz]['y'] = y
        fxy[zz]['f'] = list()
        for yy in y:
            fxy[zz]['f'].append([])
            for xx in x:
                fxy[zz]['f'][-1].append(f(xx, yy, zz))

    mat = MatrixF_ZYX(z, fxy)
    # print(mat)

    x, y, z = -0.152, 1.141, 1.43
    nx, ny, nz = 5, 5, 2
    polymon = newton_fxyz(mat, x, y, z, nx, ny, nz)
    sp = spline_fxyz(mat, x, y, z)
    print(f'polunom\t{polymon}')
    # print(f'sp\t\t{sp}')
    print(f'f()\t\t{f(x, y, z)}')


test()
