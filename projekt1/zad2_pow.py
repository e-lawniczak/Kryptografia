import random
import math


def pow_mod(x, k, n):
    """

    :param x: podstawa
    :param k: potęga zamieniana na binarną
    :param n: liczba do modulo
    :return: p - liczba x^k % n
    """
    b_k = bin(k)
    i = len(b_k) - 3
    p = 1
    while i >= 0:
        if int(b_k[i + 2]) == 1:
            p = (p * x) % n
        x = (x * x) % n
        i -= 1
    return p

def bin_pow(b, k, n):
    y = 1
    binary = list(reversed(bin(k)[2:]))
    i = len(binary) - 1
    while i >= 0:
        y = (y ** 2) % n
        if binary[i] == "1":
            y = (y * b) % n
        i = i - 1
    return y

if __name__ == '__main__':
    B = random.randint(2 ** 127, 2 ** 128)

    N = int(input("Podaj n: "))
    B = int(input("Podaj b: "))
    K = int(input("Podaj k: "))
    print(B)
#    y = pow(B, K, N)
    y = pow_mod(1088, 16, 17)
    print(y)
