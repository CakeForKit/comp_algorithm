from work_data import input_func_xyz
from MatrixF_XY import MatrixF_XY
from work_data import get_matrix_nearest_val

DEBUG = False


class MatrixF_ZYX:
    def __init__(self, filename):
        self.z, fxy = input_func_xyz(filename, printing=False)
    # def __init__(self, z, fxy):
    #     self.z = z
        # print(self.z, fxy)
        self.f_XOY = dict()
        for i, zi in enumerate(self.z):
            m = MatrixF_XY(zi, fxy[zi]['x'], fxy[zi]['y'], fxy[zi]['f'])
            self.f_XOY[i] = m

    def get_nearest_z(self, z, count):
        matrix_val_ind = [(val, i) for i, val in enumerate(self.z)]
        matrix_val_ind.sort()
        nearest_val_ind = get_matrix_nearest_val(matrix_val_ind, z, count)
        return nearest_val_ind  # [(val, ind_val), ...]

    def __str__(self):
        res = 'Matrix4d:' + '\n'
        res += f'z={self.z}' + '\n'
        for zi in self.z:
            res += f'z={zi}: {self.f_XOY[zi]}\n'
        # ff = "\n".join(map(str, self.f_XOY))
        # res += f'f={ff}' + '\n'
        return res
