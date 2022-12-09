from projekt1.zad1_euklides import inverse
from projekt1.zad2_pow import bin_pow
from projekt2.zad1_get_prime_generate_curve import curve
from projekt2.zad2_pkt_na_Fp import random_point, all_points
from projekt2.zad3_pkt_przeciwny import pkt_przeciwny


def c_lambda_1(x1, y1, A, P):
    return ((3 * bin_pow(x1, 2, P) + A) * inverse(P, (2 * y1) % P)) % P


def c_lambda_2(x1, y1, x2, y2, P):
    return ((y2 - y1) * inverse(P, (x2 - x1) % P)) % P


def c_x3(L, x1, x2, P):
    return (bin_pow(L, 2, P) - x1 - x2) % P


def c_y3(L, x3, x1, y1, P):
    return ((L * (x1 - x3)) - y1) % P


def sum_points(x1, y1, x2, y2, A, P):
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


def sum_points2(x1: int, y1: int, x2: int, y2: int, A: int,  p: int):
    if (x1, y1) == pkt_przeciwny(x2, y2, p):
        return None, None
    elif x1 == x2 and y1 == y2:
        fi = ((3 * bin_pow(x1, 2, p) + A) * inverse(p, (2 * y1) % p)) % p
        x3 = (bin_pow(fi, 2, p) - 2 * x1) % p
        return x3, (fi * (x1 - x3) - y1) % p
    else:
        fi = ((y2 - y1) * inverse(p, (x2 - x1) % p)) % p
        x3 = (bin_pow(fi, 2, p) - x1 - x2) % p
        return x3, (fi * (x1 - x3) - y1) % p


if __name__ == '__main__':
    a, b, p = curve(11)
    points = all_points(a, b, p)
    print(points)
    count = 0
    count2 = 0
    count3 = 0
    for i in range(100):
        randomPoint1 = random_point(a, b, p)
        randomPoint2 = random_point(a, b, p)
        sumPoints = sum_points(randomPoint1[0], randomPoint1[1], randomPoint2[0], randomPoint2[1], a, p)
        print("A:{} \nB:{} \np:{} \nP:{} \nQ:{}".format(a, b, p, randomPoint1, randomPoint2))
        print("R:{}".format(sumPoints))
        count = count + 1 if sumPoints in points else count
        count2 = count2 + 1 if randomPoint1 in points else count2
        count3 = count3 + 1 if randomPoint2 in points else count3
    print("Ilość poprawnych dodawań",count)
    print("Ilość poprawnych losowań 1",count2)
    print("Ilość poprawnych losowań 2",count3)
    print(points)
