from work_data import get_matrix_nearest_val


# z - const, F = f(x, y) for z
class MatrixF_XY:
    def __init__(self, zi, x_vals, y_vals, f_vals):
        self.zi = zi
        self.x = x_vals
        self.y = y_vals
        self.f = f_vals

    def get_nearest_y(self, y, count):
        matrix_val_ind = [(val, i) for i, val in enumerate(self.y)]
        matrix_val_ind.sort()
        nearest_val_ind = get_matrix_nearest_val(matrix_val_ind, y, count)
        return nearest_val_ind  # [(val, ind_val), ...]

    def get_nearest_x(self, x, count):
        matrix_val_ind = [(val, i) for i, val in enumerate(self.x)]
        matrix_val_ind.sort()
        nearest_val_ind = get_matrix_nearest_val(matrix_val_ind, x, count)
        return nearest_val_ind  # [(val, ind_val), ...]

    def get_data_nearest_x_for_yi(self, index_yi, x, polynom_nx):
        nearest_val_ind = self.get_nearest_x(x, polynom_nx + 1)
        data = []  # [(x, F), ...]
        for val, ind in nearest_val_ind:
            if self.x[ind] != val: raise Exception('yours error val_ind matrix!')
            f = self.f[index_yi][ind]
            data.append([val, f])
        return data

    def __str__(self):
        str = 'Matrix3d\n'
        str += f'\tx={self.x}\n'
        str += f'\ty={self.y}\n'
        str += f'\tf={self.f}\n'
        return str
