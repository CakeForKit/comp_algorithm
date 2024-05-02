DEBUG = True


def input_func_xyz(filename, printing=DEBUG):
    func_zyx = dict()
    z_keys = list()
    with open(filename, 'r') as file:
        z_str = file.readline()
        while z_str != '':
            try:
                z = float(z_str.strip().split('=')[1])  # inputing '   z=num  ' num = 0 1 2 3 4...
            except Exception:
                raise Exception(f'Error: format z (need "   z=float ")')

            if z in z_keys:
                raise Exception(f'Error: z={z} already inputed')
            z_keys.append(z)
            func_zyx[z] = dict()

            try:
                x_keys = list(map(float, file.readline().split()[1:]))
                func_zyx[z]['x'] = x_keys
                func_zyx[z]['y'] = []
                func_zyx[z]['f'] = []
                s = file.readline()
                while s != '\n' and s != '':
                    s = list(map(float, s.split()))
                    func_zyx[z]['y'].append(s[0])
                    func_zyx[z]['f'].append(s[1:])
                    s = file.readline()
            except Exception:
                raise Exception(f'Error: input XOY for z={z}')
            z_str = file.readline()

    if printing:
        print(f'input_func_xyz: ')
        print(f'z_keys={z_keys}')
        print(f'func_zyx={func_zyx}')

    return z_keys, func_zyx


# matrix_val_ind = [(val1, index1), (val2, index2)...] - sorted key=val
def get_matrix_nearest_val(matrix_val_ind, val, count):
    index, min_diff = 0, abs(val - matrix_val_ind[0][0])
    i = 0
    for i in range(1, len(matrix_val_ind)):
        diff = abs(val - matrix_val_ind[i][0])
        if diff < min_diff:
            index, min_diff = i, diff

    before = count // 2
    after = count - before - 1
    if index >= before and i - index >= after:
        st_ind = index - before
        end_ind = index + after
    elif index <= after:
        st_ind, end_ind = 0, count - 1
    else:
        st_ind, end_ind = i - count + 1, i

    return matrix_val_ind[st_ind:end_ind + 1]
