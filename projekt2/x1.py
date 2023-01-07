import random
#Zad 1
def odwrotnosc_euklides(my_b, N):
    a, b,  = my_b, N  
    x, y = 0, 1
    new_x, new_y = 1, 0
    while True:
        q = b//a
        buff_x = x
        buff_y = y
        x, y = new_x, new_y
        new_x = buff_x - q * new_x
        new_y = buff_y - q * new_y
        buff_a = a
        buff_b = b    
        b = buff_a
        a = buff_b - q*a

        if (a==0):
            break
    data = [new_x, new_y, a, x, y, b]
    if x < 0:
        return x + N 
    return x

#Zad 2
def binary_power(x, n, modulo):
    if n == 0:
        return 1
    if n%2 != 0:
        return (x * (binary_power(x, (n-1)//2, modulo))**2) % modulo
    return (binary_power(x, n//2, modulo)**2)%modulo


#Zad 3
def check_if_is_primary(x):
    randoms = []
    for i in range(0, 10):
        randoms.append(random.randint(0, 1000))
    for r in randoms:
        result = binary_power(r, x-1, x)
        if (result != 1):
            return False
    return True    

#Zad 4
def euler(b, p):
    result = binary_power(b, (p-1)//2, p)
    if result == 1:
        return True
    return False

#Zad 5
def pierwiastek_kwadratowy(b, p):
    if not euler(b, p):
        return False
    k = (p-3)//4
    power = binary_power(b, k+1, p)
    return power

#Zad 1
assert(odwrotnosc_euklides(3, 2**30 - 5) == 357913940)
assert(odwrotnosc_euklides(100, 54321) == 10321)

#Zad 2
assert(binary_power(3, 2**30, 2**100-1) == 404294742055422617191248672231)
assert(binary_power(10, 3**39 + 1, 2**62 + 10) == 1120803652654867934)

#Zad 3
assert(check_if_is_primary(2**201 - 313) == True)
assert(check_if_is_primary(2**201 - 323) == False)
assert(check_if_is_primary(2**33 - 9) == True)
assert(check_if_is_primary(2**33 -21) == False)

#Zad 4
assert(euler(2, 2**(201) - 313) == True)
assert(euler(3, 2**(201) - 313) == False)
assert(euler(11, 2**33 - 9 ) == True)
assert(euler(10, 2**33-9) == False)

#Zad 5
assert(pierwiastek_kwadratowy(2, 2**(201) - 313) == 3101948484103482126970424634806781703628882321291710380824411)
assert(pierwiastek_kwadratowy(3, 2**201 - 313) == False)
assert(pierwiastek_kwadratowy(11, 2**33 - 9) == 1578746474)
assert(pierwiastek_kwadratowy(10, 2**33 - 9) == False)