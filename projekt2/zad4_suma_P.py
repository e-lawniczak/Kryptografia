from projekt1.zad1_euklides import inverse
from projekt1.zad2_pow import bin_pow
from projekt2.zad1_get_prime_generate_curve import curve
from projekt2.zad2_pkt_na_Fp import random_point, all_points, is_on_curve, random_point2
from projekt2.zad3_pkt_przeciwny import pkt_przeciwny


def c_lambda_1(x1, y1, A, P):
    return ((3 * bin_pow(x1, 2, P) + A) * sub_inv(P, (2 * y1) % P)) % P


def c_lambda_2(x1, y1, x2, y2, P):
    return ((y2 - y1) * sub_inv(P, (x2 - x1) % P)) % P


def c_x3(L, x1, x2, P):
    return (L**2 - x1 - x2) % P


def c_y3(L, x3, x1, y1, P):
    return ((L * (x1 - x3)) - y1) % P


def sum_points_o(x1, y1, x2, y2, A, P):
    if None in [x1, y1]:
        return x2, y2
    if None in [x2, y2]:
        return x1, y1
    if (x1, y1) == pkt_przeciwny(x2, y2, P):
        print("Dodawanie pkt przeciwnych")
        return None, None
    lam = 0
    if x1 == x2:
        lam = c_lambda_1(x1, y1, A, P)
    else:
        lam = c_lambda_2(x1, y1, x2, y2, P)
    x3 = c_x3(lam, x1, x2, P)
    y3 = c_y3(lam, x3, x1, y1, P)
    return x3, y3


def sum_points(x1, y1, x2, y2, A, P):
    if None in [x1, y1]:
        return x2, y2
    if None in [x2, y2]:
        return x1, y1
    if x1 == x2 and y1 == -y2 % P:
        return None, None
    if x1 != x2:
        s = ((y1 - y2) * sub_inv((x1 - x2) % P, P)) % P
        x3 = (s ** 2 - x1 - x2) % P
        y3 = (s * (x1 - x3) - y1) % P
        return x3, y3
    if x1 == x2:
        s = (((3 * bin_pow(x1, 2, P)) % P + A) * sub_inv((2 * y1) % P, P)) % P
        x3 = ((bin_pow(s, 2, P) % P) - 2 * x1 % P) % P
        y3 = (s * (x1 - x3) - y1) % P
        return x3, y3
    return None, None


def sub_inv(A, B):
    return inverse(A, B)


if __name__ == '__main__':
    a, b, p = curve(300)
    count = 0
    count2 = 0
    count3 = 0
    for i in range(100):
        randomPoint1 = random_point2(a, b, p)
        randomPoint2 = random_point2(a, b, p)
        x = sum_points(randomPoint1[0], randomPoint1[1], randomPoint2[0], randomPoint2[1], a, p)
        print("\nP:{} \nQ:{}".format(randomPoint1, randomPoint2))
        print("R:{}".format(x))
        count = count + 1 if is_on_curve(x[0], x[1], a, b, p) else count
        count2 = count2 + 1 if is_on_curve(randomPoint1[0], randomPoint1[1], a, b, p) else count2
        count3 = count3 + 1 if is_on_curve(randomPoint2[0], randomPoint2[1], a, b, p) else count3
    print("Ilość poprawnych dodawań", count)
    print("Ilość poprawnych losowań 1", count2)
    print("Ilość poprawnych losowań 2", count3)
