from zad2_pow import pow


def euler(b, p):
    """
    zastosowanie twierdzenie eulera
    (a/p) = a^(p-1)/2 mod p
    :param b: podstawa - a
    :param p: liczba pierwsza
    :return: symbol Legendre'a 0 1 lub -1
    """
    return pow(b, (p - 1) // 2, p) == 1


if __name__ == '__main__':
    B = 17
    P = 104729
    print(euler(B, P))
