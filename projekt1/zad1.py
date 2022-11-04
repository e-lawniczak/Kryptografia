import random


def e_gcd(a, b):
    if a < b:
        t = a
        a = b
        b = t
    v = 0
    old_v = 1
    u = 1
    old_u = 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        old_u, u = u - q * old_u, old_u
        old_v, v = v - q * old_v, old_v
    # return a, u, v
    dzielnik = a
    y = u
    el_odwrotny = v
    if el_odwrotny > 0:
        return el_odwrotny
    return el_odwrotny % a


if __name__ == '__main__':
    n = int(input("Podaj n: "))
    b = int(input("Podaj b: "))

    x = e_gcd(n, b)
    print(x)
