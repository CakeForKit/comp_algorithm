def sympson_func(a, b, f):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def sympson_integral(x_vals, func):
    integral = 0
    for i in range(len(x_vals) - 1):
        integral += sympson_func(x_vals[i], x_vals[i + 1], func)
    return integral
