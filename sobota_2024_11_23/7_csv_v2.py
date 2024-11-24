def pobierz_dane_z_csv(nazwa_pliku = "dane.csv", separator=','):
    lista = []
    with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
        linie = plik.readlines()
        naglowki = linie[0].strip().split(separator)
        for linia in linie[1:]:
            wartosc = linia.strip().split(separator)
            slownik = {}
            for i in range(len(naglowki)):
                slownik[naglowki[i]] = wartosc[i]
            lista.append(slownik)
    return lista

lista = pobierz_dane_z_csv("dane.csv")
suma = 0
max = len(lista[0]["nazwisko"])
nazwisko = lista[0]["nazwisko"]
for pacjent in lista:
    suma += int(pacjent['wiek'])
    if max < len(pacjent["nazwisko"]):
        max = len(pacjent["nazwisko"])
        nazwisko = pacjent["nazwisko"]

    #print(pacjent['nazwisko'])
print(f"Suma lat wynosi {suma}")
print(f"Średni wiek wynosi {suma/len(lista):.0f}")
print(f"Najdłuższe nazwisko: {nazwisko}")
