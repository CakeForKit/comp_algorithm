def h_i(x_values, i):
    return x_values[i] - x_values[i - 1]


def f_i(x_values, y_values, i):
    return 3 * ((y_values[i] - y_values[i - 1]) / h_i(x_values, i) -
                (y_values[i - 1] - y_values[i - 2]) / h_i(x_values, i - 1))


def ksi_i(x_values, i, ksii_1):
    hi, hi_1 = h_i(x_values, i), h_i(x_values, i - 1)
    # ksii_1 = ksi_i(x_values, i - 1)
    return - hi / (hi_1 * ksii_1 + 2 * (hi_1 + hi))


def teta_i(x_values, y_values, i, ksii_1, tetai_1):
    fi = f_i(x_values, y_values, i)
    hi, hi_1 = h_i(x_values, i), h_i(x_values, i - 1)
    return (fi - hi_1 * tetai_1) / (hi_1 * ksii_1 + 2 * (hi_1 + hi))


# a_i = y_i-1
def calc_a_coefs(y_values):
    n = len(y_values)
    a_values = [0] * (n - 1)
    for i in range(n - 1):
        a_values[i] = y_values[i]
    return a_values


def calc_c_coefs(x_values, y_values, beg, end):
    n = len(x_values)
    c_values = [0] * (n - 1)
    ksi_values = [0] * n
    teta_values = [0] * n

    c_values[0] = beg / 2
    ksi_values[1] = 0
    teta_values[1] = beg / 2

    for i in range(2, n):
        ksi_values[i] = ksi_i(x_values, i, ksi_values[i - 1])
        teta_values[i] = teta_i(x_values, y_values, i, ksi_values[i - 1], teta_values[i - 1])

    # Cn = end / 2 and Cn+1 == 0 => Cn = tetaN+1 = end / 2
    # Cn-1 = ksi_n * Cn + teta_n = ksi_n * ksi_n-1 * Cn-1 + teta_n
    c_values[-1] = ksi_values[-1] * (end / 2) + teta_values[-1]

    for i in range(n - 2, 0, -1):
        c_values[i - 1] = c_values[i] * ksi_values[i] + teta_values[i]

    return c_values


def calc_d_coefs(x_values, c_values, end):
    n = len(x_values)
    d_values = [0] * (n - 1)
    for i in range(n - 2):
        d_values[i] = (c_values[i + 1] - c_values[i]) / (3 * h_i(x_values, i + 1))
    d_values[-1] = (end / 2 - c_values[-1]) / (3 * h_i(x_values, -1))

    # print(f'd_values = {d_values}')
    return d_values


def calc_b_coefs(x_values, y_values, c_values, end):
    n = len(x_values)
    b_values = [0] * (n - 1)

    for i in range(n - 2):
        hi = h_i(x_values, i + 1)
        b_values[i] = (y_values[i + 1] - y_values[i]) / hi - \
                      1 / 3 * hi * (c_values[i + 1] + 2 * c_values[i])
    b_values[-1] = (y_values[-1] - y_values[-2]) / h_i(x_values, -1) - \
                   h_i(x_values, -1) / 3 * (end / 2 + 2 * c_values[-1])

    # print(f'c_values = {c_values}')
    # print(f'b_values = {b_values}')
    return b_values


def calc_abcd_coefs(x_values, y_values, beg, end):
    a_values = calc_a_coefs(y_values)
    c_values = calc_c_coefs(x_values, y_values, beg, end)
    b_values = calc_b_coefs(x_values, y_values, c_values, end)
    d_values = calc_d_coefs(x_values, c_values, end)

    return a_values, b_values, c_values, d_values


def find_index_xi(x_values, x):
    n = len(x_values) - 1
    ind = 1
    while ind < n and x_values[ind] < x:
        ind += 1
    return ind - 1


def count_polynom(x_values, x, index_xi, abcd_coefs):
    h = x - x_values[index_xi]
    y = 0
    for i in range(4):
        y += abcd_coefs[i][index_xi] * (h ** i)
    return y


def spline_f_x(x_values, y_values, beg=0, end=0):

    abcd_coef = calc_abcd_coefs(x_values, y_values, beg, end)
    # with open('abcd1.txt', 'w') as f:
    #     f.write(f'{abcd_coef}\n')
    # print(f'abcd_coef - {abcd_coef}')

    def f(x):
        index_xi = find_index_xi(x_values, x)
        # print(f'index_xi = {index_xi}')

        y = count_polynom(x_values, x, index_xi, abcd_coef)
        # print(f'y = {y}')
        return y

    return f


def spline_f_xy_(x_vals, y_vals, z_vals):
    funcs_ZOX = list()
    for i in range(len(y_vals)):
        funcs_ZOX.append(spline_f_x(x_vals, z_vals[i]))

    def f(x, y):
        x0_z_vals = list()
        for i in range(len(y_vals)):
            x0_z_vals.append(funcs_ZOX[i](x))
        return spline_f_x(y_vals, x0_z_vals)(y)

    return f


