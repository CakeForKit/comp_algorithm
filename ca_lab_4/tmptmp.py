from math import sin

def func(a, b):
    x = (a + b) / 2
    f = sin(x ** 2 + 5*x)
    print(f)

func(0, 0.8)
