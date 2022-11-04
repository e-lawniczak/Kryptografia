from zad2 import pow
from zad4 import euler


def sqrt(b, p):
    if euler(b, p):
        x = pow(b, (p + 1) // 4, p)
        return x, -x
    return False, False


if __name__ == '__main__':
    B = 11
    P = 2**33 - 9

    plus, minus = sqrt(B, P)
    print(plus)
