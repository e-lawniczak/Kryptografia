import random
import math


def pow(x, k, n):
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
    X = random.randint(2 ** 127, 2 ** 128)
    # X = 18080300741509232066952834824682
    X = 3
    N = int(input("Podaj n (dziesietne): "))
    K = int(input("Podaj k (dziesietne): "))
    print(X)
    y = pow(X, K, N)
    print(y)
