from projekt1.zad3_fermat import fermat
import random

def getPrimeNumber(bits):
    k = random.randint(2 ** bits, 2 ** bits+1)
    P = 4 * k + 3
    while not fermat(P):
        P = 4 * k + 3
        k = random.randint(2 ** 300, 2 ** 301)
    return P

def delta_E(A, B, p):
    return ((4 * (A ** 3)) + (27 * B ** 2)) % p


def curve(p=-1):
    P = 1
    if p == -1:
       P = getPrimeNumber(300)
    else:
        P = p

    a = random.randint(1, P - 1)
    b = random.randint(1, P - 1)
    while delta_E(a, b, P) == 0:
        a = random.randint(1, P - 1)
        b = random.randint(1, P - 1)

    return a, b, P


if __name__ == '__main__':
    a, b, p = curve()
    print("A:{}\nB:{}\np:{}".format(a, b, p))
