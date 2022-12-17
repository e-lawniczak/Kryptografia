from projekt1.zad2_pow import bin_pow


def euler(b, p):
    """
    zastosowanie twierdzenie eulera
    (a/p) = a^(p-1)/2 mod p
    :param b: podstawa -> a
    :param p: liczba pierwsza
    :return: true jeśli jest == 1 false jeśłi nie
    """
    return bin_pow(b, (p - 1) // 2, p) == 1

def euler_0(b, p):
    """
    zastosowanie twierdzenie eulera
    (a/p) = a^(p-1)/2 mod p
    :param b: podstawa -> a
    :param p: liczba pierwsza
    :return: true jeśli jest == 1 false jeśłi nie
    """
    return bin_pow(b, (p - 1) // 2, p) > -1


if __name__ == '__main__':
    B = 17
    P = 104729
    print(euler(B, P))
