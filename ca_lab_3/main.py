from MatrixF_ZYX import MatrixF_ZYX
from newton_Matrix import newton_fxyz
from spline_Matrix import spline_fxyz
from mixed_interpol import (nns_mixed_fxyz,
                            nsn_mixed_fxyz,
                            nss_mixed_fxyz,
                            snn_mixed_fxyz,
                            sns_mixed_fxyz,
                            ssn_mixed_fxyz)
from graphic import draw_graphic

ACCURACY = 5


if __name__ == '__main__':
    matrix_F_XYZ = MatrixF_ZYX('data.txt')
    x, y, z = 1.3, 1.05, 0.82
    nx, ny, nz = 2, 2, 2

    print(f'Полиномом Ньютона: {newton_fxyz(matrix_F_XYZ, x, y, z, nx, ny, nz):.{ACCURACY}f}')
    print(f'Сплайн: {spline_fxyz(matrix_F_XYZ, x, y, z):.{ACCURACY}f}')

    print(f'Смешанная интерполяция (x - Ньютон, y - Ньютон, z - Сплайн): '
          f'{nns_mixed_fxyz(matrix_F_XYZ, x, y, z, nx, ny):.{ACCURACY}f}')

    print(f'Смешанная интерполяция (x - Ньютон, y - Сплайн, z - Ньютон): '
          f'{nsn_mixed_fxyz(matrix_F_XYZ, x, y, z, ny, nz):.{ACCURACY}f}')

    print(f'Смешанная интерполяция (x - Ньютон, y - Сплайн, z - Сплайн): '
          f'{nss_mixed_fxyz(matrix_F_XYZ, x, y, z, ny):.{ACCURACY}f}')

    print(f'Смешанная интерполяция (x - Сплайн, y - Ньютон, z - Ньютон): '
          f'{snn_mixed_fxyz(matrix_F_XYZ, x, y, z, nx, nz):.{ACCURACY}f}')

    print(f'Смешанная интерполяция (x - Сплайн, y - Ньютон, z - Сплайн): '
          f'{sns_mixed_fxyz(matrix_F_XYZ, x, y, z, nx):.{ACCURACY}f}')

    print(f'Смешанная интерполяция (x - Сплайн, y - Сплайн, z - Ньютон): '
          f'{ssn_mixed_fxyz(matrix_F_XYZ, x, y, z, nz):.{ACCURACY}f}')
    draw_graphic(matrix_F_XYZ)

