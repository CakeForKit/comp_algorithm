import numpy as np
from matplotlib import pyplot as plt


def draw_graphic_xy(data, func, func1):
    xmin = min(data, key=lambda elem: elem.x).x
    xmax = max(data, key=lambda elem: elem.x).x
    x_vals = np.linspace(xmin, xmax, 100)

    plt.figure("График функции")
    plt.ylabel("Y")
    plt.xlabel("X")

    for p in data:
        plt.plot(p.x, p.y, 'r.')

    y_vals = func(x_vals)
    plt.plot(x_vals, y_vals, 'r', label="y = f(x)")
    y_vals1 = func1(x_vals)
    plt.plot(x_vals, y_vals1, 'b', label="y = f(x) p=1")

    plt.legend()
    plt.show()


def get_coord_points(data):
    xp, yp, zp = list(), list(), list()
    for p in data:
        xp.append(p.x)
        yp.append(p.y)
        zp.append(p.z)
    return np.array(xp), np.array(yp), np.array(zp)


def make_3d_grid(xvals, yvals, func):
    xGrid, yGrid = np.meshgrid(xvals, yvals)
    zGrid = np.array([[
        func(
            xGrid[i][j],
            yGrid[i][j],
        ) for j in range(len(xvals))
    ] for i in range(len(yvals))])
    return xGrid, yGrid, zGrid


def draw_graphic_xyz(data, func):
    xmin = min(data, key=lambda elem: elem.x).x
    xmax = max(data, key=lambda elem: elem.x).x
    x_vals = np.linspace(xmin, xmax, 100)

    ymin = min(data, key=lambda elem: elem.y).y
    ymax = max(data, key=lambda elem: elem.y).y
    y_vals = np.linspace(ymin, ymax, 100)

    xpoints, ypoints, zpoints = get_coord_points(data)

    fig = plt.figure("График функции")
    axes = fig.add_subplot(projection='3d')
    axes.scatter(xpoints, ypoints, zpoints, c='red')
    axes.set_xlabel('OX')
    axes.set_ylabel('OY')
    axes.set_zlabel('OZ')

    x_vals, y_vals, z_vals = make_3d_grid(x_vals, y_vals, func)
    axes.plot_surface(x_vals, y_vals, z_vals)
    plt.show()
    #
    # for p in data:
    #     plt.plot(p.x, p.y, 'r.')
    #
    # y_vals = func(x_vals)
    # plt.plot(x_vals, y_vals, 'r', label="y = f(x)")
    # y_vals1 = func1(x_vals)
    # plt.plot(x_vals, y_vals1, 'b', label="y = f(x) p=1")
    #
    # plt.legend()
    # plt.show()


def draw_graphic_diffur(xval, f, fm2, fm3):
    y = f(xval)
    ym2 = fm2(xval)
    ym3 = fm3(xval)

    plt.figure("График функции")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.plot(xval, y, 'r', label="original")
    plt.plot(xval, ym2, 'g', label="m = 2")
    plt.plot(xval, ym3, 'b', label="m = 3")
    plt.legend()
    plt.show()