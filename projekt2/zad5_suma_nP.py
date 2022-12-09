from projekt2.zad1_get_prime_generate_curve import curve
from projekt2.zad2_pkt_na_Fp import random_point, all_points
from projekt2.zad3_pkt_przeciwny import pkt_przeciwny
from projekt2.zad4_suma_P import sum_points, sum_points2

points = []


def sum_n_points(x, y, A, P, N):
    x1 = x
    y1 = y
    x2 = x
    y2 = y
    x3 = None
    y3 = None
    count = 0
    while count < N - 1:
        (x3, y3) = sum_points(x1, y1, x2, y2, A, P)
        count += 1
        if (x3, y3) == pkt_przeciwny(x, y, P):
            print("Wynik dodawania #{} to element przeciwny do P:{}\n{}R:{}".format(count + 1, (x, y), count + 1,
                                                                                    (x3, y3)))
            return None, None
        if (x3, y3) not in points:
            print("Punkt {} nie znajduje się w zbiorze punktów Fp. count:{}".format((x3, y3), count + 1))
            print(points)
        x1 = x3
        y1 = y3
    return x1, y1


if __name__ == '__main__':
    a, b, p = curve(11)
    points = all_points(a, b, p)
    for i in range(100):
        print("\ni:{}  ===================================================\n".format(i))
        randomPoint1 = random_point(a, b, p)
        n = i  # i if i < 30 else 30
        print("A:{} \nB:{} \np:{} \nP:{} ".format(a, b, p, randomPoint1))
        sumNPoints = sum_n_points(randomPoint1[0], randomPoint1[1], a, p, n)
        print("{}*P:{}".format(n, sumNPoints))
    print(points)
