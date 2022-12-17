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
        return el_odwrotny
    return el_odwrotny % a


def inverse_2(n, b):
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


def inverse(A, B):
    a, b, = A, B
    x, y = 0, 1
    new_x, new_y = 1, 0
    while True:
        q = b // a
        buff_x = x
        buff_y = y
        x, y = new_x, new_y
        new_x = buff_x - q * new_x
        new_y = buff_y - q * new_y
        buff_a = a
        buff_b = b
        b = buff_a
        a = buff_b - q * a

        if (a == 0):
            break
    data = [new_x, new_y, a, x, y, b]
    if x < 0:
        return x + B
    return x


if __name__ == '__main__':
    n = int(input("Podaj n: "))
    b = int(input("Podaj b: "))

    x = e_gcd(n, b)
    print(x)
