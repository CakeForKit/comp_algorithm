from slauNewton import newton_slau

def f1(x, y, z):
    return x ** 2 + y ** 2 + z ** 2 - 1


def f2(x, y, z):
    return 2 * x ** 2 + y ** 2 - 4 * z


def f3(x, y, z):
    return 3 * x ** 2 - 4 * y + z ** 2

SYSTEM = [f1, f2, f3]

def jacobian(x, y, z):
    return [
        [2 * x, 2 * y, 2 * z],
        [4 * x, 2 * y, -4],
        [6 * x, -4, 2 * z]
    ]


if __name__ == '__main__':
    xyz0 = [0.5, 0.5, 0.5]
    eps = 1e-2
    res = newton_slau(jacobian, SYSTEM, xyz0, eps, True)

    print(f'Точность={eps}, нач приближение = {xyz0}')
    print(f'Рещение = {res}')

    acc = 10
    rf1, rf2, rf3 = f1(*res), f2(*res), f3(*res)
    print(f'Проверка подстановкой: {rf1:.{acc}f}, {rf2:.{acc}f}, {rf3:.{acc}f}')
