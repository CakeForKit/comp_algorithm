from newton import polynom_newton

EPS = 1e-5


def bin_search_zero_y(data, x1, y1, x2, y2):
    # print(x1, y1, x2, y2)
    n = 5
    cx = (x1 + x2) / 2
    cy = polynom_newton(data, cx, n, False)
    if abs(cy) < EPS:
        return cx
    elif cy * y1 < 0:
        return bin_search_zero_y(data, x1, y1, cx, cy)
    else:
        return bin_search_zero_y(data, cx, cy, x2, y2)


def find_root(data):
    i1, i2 = 0, 1
    while data[i1][1] * data[i2][1] > 0:
        i1 += 1
        i2 += 1
        # предполагается что данные поступают верные и в них есть y с разными знаками как по условию
        if i2 >= len(data):
            raise Exception('MY_ERROR: find_root: Wrong_data')

    return bin_search_zero_y(data, data[i1][0], data[i1][1], data[i2][0], data[i2][1])


