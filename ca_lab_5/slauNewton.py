from gauss import gauss


def newton_slau(mtrx_jacobian, funcs: list, x0: list, eps, printing=False):
    xk = x0
    # iters = 1
    while True:
        slau = mtrx_jacobian(*xk)
        for i, f in enumerate(funcs):
            slau[i].append(-f(*xk))

        dx = gauss(slau, printing)
        xnext = [xk[i] + dx[i] for i in range(len(xk))]
        xk = xnext

        if max(abs(dx[i] / xk[i]) for i in range(len(dx))) < eps:
            return xk

