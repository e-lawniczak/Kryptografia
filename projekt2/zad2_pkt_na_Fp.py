from projekt1.zad2_pow import pow_mod, bin_pow
from projekt1.zad4_euler import euler
from projekt1.zad5_reszty_kw import sqr, sqr_e
from projekt2.zad1_get_prime_generate_curve import curve
import random


def curve_eq(X, A, B, P):
    return (bin_pow(X, 3, P) + A * X + B) % P


def all_points(A, B, P):
    points = []
    for i in range(P):
        f = curve_eq(i, A, B, P)
        if euler(f, P):
            (y1, y2) = sqr_e(f, P)
            points.append((i, y1))
            points.append((i, y2))
    return points


def random_point(A, B, P):
    if P % 4 != 3:
        raise Exception("p%4 != 3")
    x = random.randint(0, P - 1)
    y2 = curve_eq(x, A, B, P)
    while bin_pow(y2, (P - 1) // 2, P) == -1:
        x = random.randint(0, P - 1)
        y2 = curve_eq(x, A, B, P)

    plus_y, minus_y = sqr_e(y2, P)
    # print("Wylosowane punkty ({},{}), ({},{}) nad E/F{}".format(x, plus_y, x, minus_y, P))
    return x, plus_y


if __name__ == '__main__':
    a, b, p = curve()
    print("A:{} \nB:{} \np:{} \nP:{}".format(a, b, p, random_point(10, 2, p)))
    print(curve_eq(8,10,2,p))
    print(0, 11)
    print(bin_pow(0, (p + 1) // 4, p))
    print(all_points(10,2,p))
