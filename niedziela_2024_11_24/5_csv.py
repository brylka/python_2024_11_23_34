import csv

def pobierz_dane_z_csv(nazwa_pliku = "dane.csv", separator=','):
    lista = []
    with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
        linie = csv.DictReader(plik, delimiter=separator)
        for wiersz in linie:
            lista.append(wiersz)
    return lista


lista = pobierz_dane_z_csv("dane.csv")
print(lista)
suma = 0
max = len(lista[0]["nazwisko"])
nazwisko = lista[0]["nazwisko"]
for pacjent in lista:
    suma += int(pacjent['wiek'])
    if max < len(pacjent["nazwisko"]):
        max = len(pacjent["nazwisko"])
        nazwisko = pacjent["nazwisko"]

print(f"Suma lat wynosi {suma}")
print(f"Średni wiek wynosi {suma/len(lista):.0f}")
print(f"Najdłuższe nazwisko: {nazwisko}")
