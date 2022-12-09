from zad2_pow import pow
from zad4_euler import euler


def sqr(b, p):
    """
    Sprawdza czy podana liczba jest resztą kwadratową
    :param b: liczba do sprawdzenia
    :param p: liczba pierwsza
    :return: x p-x: reszty kwadratowe lub False, False gdy b nie jest resztą kwadratową
    """
    if euler(b, p):
        x = pow(b, (p + 1) // 4, p)
        return x, p-x
    return False, False


if __name__ == '__main__':
    B = 10
    P = 2 ** 32

    plus, minus = sqr(B, P)
    print(plus)
