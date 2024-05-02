from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from MatrixF_ZYX import MatrixF_ZYX

def draw_graphic(mat: MatrixF_ZYX):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = 0
    data_zind = mat.z.index(round(z))
    x_1 = mat.f_XOY[data_zind].x
    y_1 = mat.f_XOY[data_zind].y
    x_1, y_1 = np.meshgrid(x_1, y_1)
    data_z1 = mat.f_XOY[data_zind].f
    data_z1 = np.array(data_z1)

    # print(f'x_1={x_1}')
    # print(f'y_1={y_1}')
    # print(f'data_z1={data_z1}')


    surf = ax.plot_surface(x_1, y_1, data_z1, cmap='plasma', rstride=1, cstride=1, label=f'z={z}', antialiased=True)
    fig.colorbar(surf)
    plt.show()



if __name__ == '__main__':
    matrix_F_XYZ = MatrixF_ZYX('data.txt')
    draw_graphic(matrix_F_XYZ)