import random
from projekt1.zad2_pow import pow_mod, bin_pow


def fermat(n, k=100):
    """

    :param n: podejrzana liczba pierwsza
    :param k: liczba testów fermata do wykonania domyślnie 100
    :return: True jeśli liczba jest pierwsza, False jeśli nie jest
    """
    tests = [random.randint(0, 5000) for i in range(k)]

    for t in tests:
        if bin_pow(t, n - 1, n) != 1:
            return False
    return True


if __name__ == '__main__':
    N = 104593 

    print(fermat(N))
    # countT = 0
    # countF = 0
    # for i in range(10000):
    #     if fermat(N) == False:
    #         countF += 1
    #     if fermat(N) == True:
    #         countT += 1
    # print("{} jest pierwsze: {}".format(N, countT))
    # print("{} nie jest pierwsze: {}".format(N, countF))

