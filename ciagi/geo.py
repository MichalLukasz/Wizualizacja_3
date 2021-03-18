def wyraz(a1, n, q):
    wynik = a1 * q ** (n - 1)
    return wynik


def suma(a1, n, q):
    if q == 1:
        wynik = a1 * n
    else:
        wynik = a1 * (1 - q ** n) / (1 - q)
    return wynik
