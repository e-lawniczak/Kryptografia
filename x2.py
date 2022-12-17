import random
import miniprojekt_1


class EllipticCurve():
    INFTY = 'infty'

    def __init__(self, p) -> None:
        self.p = p
        self.A = 0
        self.B = 1
        self.elliptic_curve_equation = x**3+ self.A * x+ self.B

    def check_if_point_is_on_curve(self, x, y):
        if (y**2 % self.p) == (x**3 + self.A*x + self.B) % self.p:
            return True    
        return False     

    def generate_specific_elliptic_curve(self, p, A, B):
        self.p = p
        self.A = A
        self.B = B

    def generate_random_elliptic_curve(self):
        self.A = random.randint(1, self.p -1)
        self.B = random.randint(1, self.p -1)
        delta = (4*self.A**3 + 27*self.B**2) % self.p
        if delta == 0:
            return self.generate_random_elliptic_curve()
    
    def get_random_point(self):
        x = random.randint(1, self.p-1)
        equation = (x**3 + self.A*x + self.B) % self.p
        y = miniprojekt_1.pierwiastek_kwadratowy(equation, self.p)
        if y:
            return (x, y)
        else:
            return self.get_random_point()
            
    
    def get_point_inverse(self, x, y):
        if x == self.INFTY or y == self.INFTY:
            return self.INFTY, self.INFTY
        return x, -y%self.p

    def point_sum(self, x_p, y_p, x_q, y_q):
        if self.INFTY in [x_p, y_p]:
            return x_q, y_q
        if self.INFTY in [x_q, y_q]:
            return x_p, y_p
        if x_p != x_q:
            s = ((y_p - y_q) * miniprojekt_1.odwrotnosc_euklides((x_p - x_q) % self.p, self.p)) % self.p
            x_r = (s**2 - x_p - x_q) % self.p
            y_r = (s*(x_p - x_r) - y_p) % self.p
            return x_r, y_r
        if x_p == x_q and y_p == y_q:
            s = (((3* miniprojekt_1.binary_power(x_p, 2, self.p)) % self.p + self.A) * miniprojekt_1.odwrotnosc_euklides((2*y_p) % self.p, self.p)) % self.p 
            x_r = ((miniprojekt_1.binary_power(s, 2, self.p) % self.p) - 2*x_p % self.p) % self.p
            y_r = (s*(x_p - x_r) - y_p) % self.p
            return x_r, y_r
        return self.INFTY, self.INFTY

    def wielokrotnosc(self, x, y, n):
        x_buff = x
        y_buff = y
        x_r = self.INFTY
        y_r = self.INFTY
        while n > 0:
            if n % 2 == 1:
                x_r, y_r = self.point_sum(x_r,y_r, x_buff, y_buff)
                n = n - 1
            x_buff, y_buff = self.point_sum(x_buff, y_buff, x_buff, y_buff)
            n = n // 2
        return x_r, y_r

# #Zadanie 1 Losowa krzywa eliptyczna
# print('Zadanie 1 - Losowy parametr A i B')
# elliptic_curve = EllipticCurve(4111)
# elliptic_curve.generate_random_elliptic_curve()
# print(elliptic_curve.A, elliptic_curve.B)
# print()

# #Zadanie 2 Losowy punkt
# print('Zadanie 2 - Losowy punkt')
# x, y = elliptic_curve.get_random_point()
# print(x, y, 'sa prawidłowe? - ', elliptic_curve.check_if_point_is_on_curve(x, y))
# print()

# # Zadanie 3 Punkt przeciwny
# print('Zadanie 3 - Punkt przeciwny, przykład 1:')
# elliptic_curve.generate_specific_elliptic_curve(7, 2, 4)
# x, y = elliptic_curve.get_point_inverse(3, 4)
# print(x, y)
# assert x == 3 and y == 3
# print()

# print('Punkt przeciwny, przykład 2:')
# elliptic_curve.generate_specific_elliptic_curve(7, 2, 4)
# x, y = elliptic_curve.get_point_inverse(EllipticCurve.INFTY, EllipticCurve.INFTY)
# print(x, y)
# assert x == EllipticCurve.INFTY and y == EllipticCurve.INFTY
# print()

# print('Punkt przeciwny, przykład 3:')
# elliptic_curve.generate_specific_elliptic_curve(68719476731, 2645887931, 63508942644)
# x, y = elliptic_curve.get_point_inverse(56174319723, 50334202836)
# print(x, y)
# assert x == 56174319723 and y == 18385273895
# print()


# #zadanie 4
# print('Zadanie 4 Przykład 1:')
# zad_4_curve = EllipticCurve(7)

# zad_4_curve.generate_specific_elliptic_curve(68719476731, 2645887931, 63508942644)
# x_r, y_r = zad_4_curve.point_sum(56174319723, 50334202836, 15593395299, 42666859491)
# print(x_r, y_r)
# assert x_r == 19207335924 and y_r == 50314146460
# print()

# print('Przykład 2:')
# zad_4_curve.generate_specific_elliptic_curve(68719476731, 20850939805, 59338401596)
# x_r, y_r = zad_4_curve.point_sum(3789244612, 16129056986, 3789244612, 52590419745)
# print(x_r, y_r)
# assert x_r == zad_4_curve.INFTY and y_r == zad_4_curve.INFTY
# print()

# print('Przykład 3:')
# zad_4_curve.generate_specific_elliptic_curve(68719476731, 49710749469, 5286130045)
# x_r, y_r = zad_4_curve.point_sum(24069898531, 10203122697, 24069898531, 10203122697)
# print(x_r, y_r)
# assert x_r == 59980568326 and y_r == 67335054959
# print()

# print('Przykład 4:')
# zad_4_curve.generate_specific_elliptic_curve(7, 2, 4)
# x_r, y_r = zad_4_curve.point_sum(3, 4, 0, 2)
# print(x_r, y_r)
# assert x_r == 6 and y_r == 1
# print()


# # zadanie 5
# print('Zadanie 5 Przykład 1:')
# zad5_curve = EllipticCurve(11)
# zad5_curve.generate_specific_elliptic_curve(11, 3, 5)
# x, y = zad5_curve.wielokrotnosc(0, 4, 4)
# print(x, y)
# assert x == 10 and y == 1
# print()

# print('Przykład 2:')
# zad5_curve.generate_specific_elliptic_curve(1298074214633706907132624082305003, 228534005990621198360294597781867, 569902189632523536847978118572132)
# x, y = zad5_curve.wielokrotnosc(149381772199891494705202718572565, 409260229456564272828054179242535, 1298074214633706907132624082305000)
# print(x, y)
# assert x == 986078474331561338747222244192406 and y == 762094002267112631659808038096452

