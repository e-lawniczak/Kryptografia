from projekt1.zad3 import fermat
import random


def delta_E(A, B, p):
    return ((4 * (A ** 3)) + (27 * B ** 2)) % p


def curve(p=-1):
    P = 1
    if p == -1:
        k = random.randint(2 ** 300, 2 ** 301)
        P = 4 * k + 3
        while not fermat(P):
            P = 4 * k + 3
            k = random.randint(2 ** 300, 2 ** 301)
    else:
        P = p

    a = random.randint(1, P - 1)
    b = random.randint(1, P - 1)
    while delta_E(a, b, P) == 0:
        a = random.randint(1, P - 1)
        b = random.randint(1, P - 1)

    return a, b, P


if __name__ == '__main__':
    a, b, p = curve(13)
    print("A:{}\nB:{}\np:{}".format(a, b, p))
