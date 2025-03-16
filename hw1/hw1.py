import random

def hill_climb(func, a, b, c, step=0.01):
    while True:
        val = func(a, b, c)
        print(f'a={a:.3f} b={b:.3f} c={c:.3f} func(a,b,c)={val:.3f}')
        if func(a+step, b, c) >= val:
            a += step
        elif func(a-step, b, c) >= val:
            a -= step
        elif func(a, b+step, c) >= val:
            b += step
        elif func(a, b-step, c) >= val:
            b -= step
        elif func(a, b, c+step) >= val:
            c += step
        elif func(a, b, c-step) >= val:
            c -= step
        else:
            break
    return a, b, val

def function(x, y, z):
    return -1 * (x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8)

hill_climb(function, 0, 0, 0)
