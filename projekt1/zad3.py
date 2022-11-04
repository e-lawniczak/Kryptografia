import random
from zad2 import pow


def fermat(n, k=10):
    tests = [random.randint(0, 5000) for i in range(k)]

    for t in tests:
        if pow(t, n - 1, n) != 1:
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

