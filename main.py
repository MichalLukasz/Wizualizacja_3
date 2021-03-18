import random
import sys
from ciagi import *

print('Zadanie 1')
A = [1 - x for x in range(1, 11)]
print(A)
B = [3 ** x for x in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

print('Zadanie 2')
lista1 = []
for i in range(10):
    n = random.randint(1, 100)
    lista1.append(n)
print(lista1)
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista2)

print('Zadanie 3')
prod = {"Jabłka": "kg",
        "Mleko 400ml": "szt",
        "Czereśnie": "kg",
        "Jogurt": "szt",
        "Cukier 500g": "szt",
        "Cukierki": "kg"}
lista_szt = {key: value for key, value in prod.items() if value == "szt"}
print(prod)
print(lista_szt)

print('Zadanie 4')


def trojkat_pr(x, y, z):
    # sprawdzam, który bok jest najdłuższy
    a = x
    b = y
    c = z
    if x > c:
        a = z
        b = y
        c = x
    if y > c:
        a = z
        b = x
        c = y
    # wg twierdzenia Pitagorasa
    if a ** 2 + b ** 2 == c ** 2:
        return "Trójkąt jest prostokątny"
    else:
        return "Trójkąt nie jest prostokątny"


sys.stdout.write("Podaj długość 3 boków trójkąta: \n")
l1 = sys.stdin.readline()
l2 = sys.stdin.readline()
l3 = sys.stdin.readline()
l1 = int(l1)
l2 = int(l2)
l3 = int(l3)

print(trojkat_pr(l1, l2, l3))

print('Zadanie 5')


def pole_trapezu(a=9, b=3, h=3):
    return ((a + b) * h) / 2


print("Pole trapezu a=9, b=3, h=3 to: \n", pole_trapezu())

print('Zadanie 6')


def ciag(a1=1, b=4, ile=10):
    an = 1
    for ile in range(ile):
        an = a1 * b ** ile
    return an


# wynikiem jest n-ty wyraz ciągu
print(ciag())

print('Zadanie 7')


def ciag_2(*liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
    for x in range(liczby[-1]):
        iloczyn = liczby[0] * liczby[1] ** x
    return iloczyn


print(ciag_2(1, 4, 10))

print('Zadanie 8')


def to_lubie(**rzeczy):
    print('Ilość produktów:', len(rzeczy))
    wynik = 0
    for cos in rzeczy:
        wynik += rzeczy[cos]
    print('Wartość zakupów:', wynik)


to_lubie(Koszula=79.99,
         Kurtka=199.99,
         Spodnie=99.99,
         Tshirt=49.99,
         Buty=179.99,
         Rekawice=49.99)

print('Zadanie 9')
print('n-ty wyraz ciągu aryt:', ary.wyraz(1, 5, 3))
print('suma n wyrazów ciągu aryt:', ary.suma(1, 13, 5))
print('n-ty wyraz przez sumę:', ary.wyr_sum(35, 22))
print('n-ty wyraz ciągu geo:', geo.wyraz(2, 3, 4))
print('suma n wyrazów ciągu geo:', geo.suma(2, 3, 4))

print('Zadanie 10')
plik = open("liczby.txt", "w")
n = 0
while n <= 10:
    los = random.randint(1, 100)
    if los % 4 == 0:
        n += 1
        los = str(los)
        plik.write(los)
        plik.write(", ")
plik.close()


print('Zadanie 11')
plik = open("liczby.txt", "r")
linia = plik.readline()
plik.close()
print(linia)
