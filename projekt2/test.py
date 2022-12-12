import math

from projekt1.zad2_pow import bin_pow
from projekt1.zad4_euler import euler
from projekt1.zad5_reszty_kw import sqr
from projekt2.zad1_get_prime_generate_curve import curve
from projekt2.zad2_pkt_na_Fp import random_point
from projekt2.zad3_pkt_przeciwny import pkt_przeciwny
from projekt2.zad4_suma_P import sum_points
from projekt2.zad5_suma_nP import sum_n_points


def encode(A, B, M, mi, p):
    for j in range(mi):
        x = (M * mi + j) % p
        f = (bin_pow(x, 3, p) + A * x + B) % p
        if euler(f, p) == 1:
            y1, y2 = sqr(f, p)

    return x, y1


def decode(x, mi):
    return math.floor((x - 1) / mi)


if __name__ == '__main__':
    a, b, p = curve()
    n = 12
    (x1, y1) = random_point(a, b, p)
    (x2, y2) = random_point(a, b, p)
    (x1, minus_y1) = pkt_przeciwny(x1, y1, p)
    (x3, y3) = sum_points(x1, y1, x2, y2, a, p)
    (x, y) = sum_points(x1, y1, x1, minus_y1, a, p)
    (x4, y4) = sum_n_points(x1, y1, a, p, n)

    print(
        """
        E/F{}: 
        Y^2 = X^3 + {}X + {}
    
        P: {} 
        -P: {}
        Q: {}
        P + Q: {}
        neutralny = {}
        {}P: {}
        """.format(p, a, b, (x1, y1), (x1, minus_y1), (x2, y2), (x3, y3), (x, y), n, (x4, y4))
    )
