import math

from projekt1.zad2_pow import bin_pow
from projekt1.zad4_euler import euler
from projekt1.zad5_reszty_kw import sqr
from projekt2.zad1_get_prime_generate_curve import curve
from projekt2.zad2_pkt_na_Fp import random_point
from projekt2.zad3_pkt_przeciwny import pkt_przeciwny
from projekt2.zad4_suma_P import sum_points
from projekt2.zad5_suma_nP import sum_n_points_bin, sum_n_points
import random


def test():
    a, b, p = curve()
    Q = random_point(a, b, p)
    Px = Q[0]
    Py = Q[1]
    print("E: ", a, b, p)
    print("P: ", Px, Py)

    x_a = random.randint(1, p // 2)
    x_b = random.randint(1, p // 2)
    print("x_a:", x_a)
    print("x_b:", x_b)

    Q_ax, Q_ay = sum_n_points_bin(Px, Py, a, p, x_a)
    Q_bx, Q_by = sum_n_points_bin(Px, Py, a, p, x_b)

    S_a = sum_n_points_bin(Q_bx, Q_by, a, p, x_a)
    S_b = sum_n_points_bin(Q_ax, Q_ay, a, p, x_b)

    print("S_a == S_b: ", S_a == S_b)
    print("S_a: ", S_a)
    print("S_b: ", S_b)


if __name__ == '__main__':
    """
    Diffie-helman na krzywych eliptycznych
    1. Generujemy krzywą e: A, B, p
    2. Losujemy punkt P na krzywej
    
    Alice:
    1. losuj 1<x_a<1/2p
    2. oblicz Q_a = x_a * P
    3. Prześlij Q_a
    
    Bob
    1. losuj 1<x_b<1/2p
    2. oblicz Q_b = x_b * P
    3. Prześlij Q_b
    
    Po wymienie kluczy 
    1. Oblicz S = x_a * Q_b - sekret alice
    2. Oblicz S = x_b * Q_a - sekret boba
    
    
    """
    test()
    # a, b, p = curve(11)
    # n = 12
    # (x1, y1) = random_point(a, b, p)
    # (x2, y2) = random_point(a, b, p)
    # (x1, minus_y1) = pkt_przeciwny(x1, y1, p)
    # (x3, y3) = sum_points(x1, y1, x2, y2, a, p)
    # (x, y) = sum_points(x1, y1, x1, minus_y1, a, p)
    # (x4, y4) = sum_n_points(x1, y1, a, p, n)
    # (x5, y5) = sum_n_points_bin(x1, y1, a, p, n)
    # # a = 1 b = 7, P(5,4) Q (6,3)
    # print(
    #     """
    #     E/F{}:
    #     Y^2 = X^3 + {}X + {}
    #
    #     P: {}
    #     -P: {}
    #     Q: {}
    #     P + Q: {}
    #     neutralny = {}
    #     {}P: {}
    #     """.format(p, a, b, (x1, y1), (x1, minus_y1), (x2, y2), (x3, y3), (x, y), n, (x4, y4))
    # )
    # print(x4, y4)
    #
    # print(x5, y5)
