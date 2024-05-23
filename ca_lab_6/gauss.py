from in_output import print_slau


def to_triangle_mtrx(mtrx):
    n = len(mtrx)
    for k in range(n):
        for i in range(k + 1, n):
            coeff = -(mtrx[i][k] / mtrx[k][k])
            for j in range(k, n + 1):
                mtrx[i][j] += coeff * mtrx[k][j]

    return mtrx


def gauss(slau, printing=True):
    n = len(slau)

    slau = to_triangle_mtrx(slau)

    if printing:
        print("\nТреугольный вид матрицы:")
        print_slau(slau)

    # обратный зод
    result = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            slau[i][n] -= result[j] * slau[i][j]

        result[i] = slau[i][n] / slau[i][i]
    return result
