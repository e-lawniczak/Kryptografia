import random
import math


def pow(x, k, n):
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


if __name__ == '__main__':
    B = random.randint(2 ** 127, 2 ** 128)

    N = int(input("Podaj n: "))
    B = int(input("Podaj b: "))
    K = int(input("Podaj k: "))
    print(B)
#    y = pow(B, K, N)
    y = pow(1088, 16, 17)
    print(y)
