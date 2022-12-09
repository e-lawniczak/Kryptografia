from projekt2.zad1_get_prime_generate_curve import curve
from projekt2.zad2_pkt_na_Fp import random_point


def pkt_przeciwny(X, Y, P):
    return X, P - Y


if __name__ == '__main__':
    a, b, p = curve(11)
    randomPoint = random_point(a, b, p)
    print("A:{} \nB:{} \np:{} \nP:{}".format(a, b, p, randomPoint))
    print("Punkt przeciwny do P:{} \n R:{}".format(randomPoint, pkt_przeciwny(randomPoint[0], randomPoint[1], p)))
