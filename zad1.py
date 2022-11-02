import random


def e_gcd(a, b):

    if a < b:
        t = a
        a = b
        b = t
    N = a
    X = b
    v = 0
    old_v = 1
    u = 1
    old_u = 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        old_u, u = u - q * old_u, old_u
        old_v, v = v - q * old_v, old_v
    return a, u, v


if __name__ == '__main__':
    n = int(input("Podaj n: "))
    b = int(input("Podaj b: "))
    # a = 17
    # b = 5

    d, y, x = e_gcd(n, b)
    print("NWD({},{}) = {} = {} * {} + {} * {}".format(n, b, d, n, x, b, y))
    print("Elementem odwrotnym do {} w grupie mod {} jest: {}".format(b, n, x % n))
    print((b * x%n) % n)

