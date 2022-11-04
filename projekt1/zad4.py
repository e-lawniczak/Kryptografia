from zad2 import pow


def euler(b, p):
    return pow(b, (p - 1) // 2, p) == 1


if __name__ == '__main__':
    B = 17
    P = 104729
    print(euler(B, P))
