import random


def e_gcd(a, b):
    """
    rozszerzony algorytm euklidesa

    :param a:
    :param b:
    :return: (element odwrotny, NWD)
    """
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
        return el_odwrotny, dzielnik
    return el_odwrotny % a, dzielnik

def inverse(n, b):
    A = n
    B = b
    U = 0
    V = 1
    while B != 0:
        q = A // B
        temp = A
        A = B
        B = temp + (-q * B)
        temp = U
        U = V
        V = temp + (-q * V)
    if U < 0:
        return n + U
    return U

if __name__ == '__main__':
    n = int(input("Podaj n: "))
    b = int(input("Podaj b: "))

    x = e_gcd(n, b)
    print(x)
