from numpy import linspace


# return data = [x_vals: list, y_vals: list, z_vals[y][x]: dict]
def read_data(filename):
    y_vals = list()
    z_vals = list()
    with open(filename, 'r') as file:
        x_vals = list(map(float, file.readline().split()[1:]))
        file.readline()

        line = file.readline()
        while line != '':
            line = list(map(float, line.split()))
            y_vals.append(line[0])
            z_vals.append(line[1:])

            line = file.readline()

    return x_vals, y_vals, z_vals


def generate_data_by_func(func, xb, xe, yb, ye, step):
    # xb, xe = -2, 2
    # yb, ye = -2, 2
    # step = 0.1
    num = int((xe - xb) / step)

    x_vals = list(linspace(xb, xe, num))
    y_vals = list(linspace(yb, ye, num))
    z_vals = list()
    for y in y_vals:
        z_vals.append([])
        for x in x_vals:
            z_vals[-1].append(func(x, y))

    return x_vals, y_vals, z_vals