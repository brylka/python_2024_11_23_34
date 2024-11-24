lista = []
with open("dane.csv", mode='r', encoding='utf-8') as plik:
    linie = plik.readlines()

    naglowki = linie[0].strip().split(",")

    for linia in linie[1:]:
        wartosc = linia.strip().split(",")
        slownik = {}
        for i in range(len(naglowki)):
            slownik[naglowki[i]] = wartosc[i]
        lista.append(slownik)

for linia in lista:
    print(linia)