import csv

class Dane:
    def __init__(self):
        self.lista = []

    def pobierz_dane_z_csv(self, nazwa_pliku, separator=','):
        self.lista = []
        with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
            linie = csv.DictReader(plik, delimiter=separator)
            for wiersz in linie:
                self.lista.append(wiersz)
        if len(self.lista) > 0:
            print(f"Dane wczytane, ilość rekordów: {len(self.lista)}")
        else:
            print(f"Coś poszło nie tak.")

    def suma_lat(self):
        suma = 0
        for pacjent in self.lista:
            suma += int(pacjent['wiek'])
        return suma

dane = Dane()
dane.pobierz_dane_z_csv("dane.csv")
print(dane.suma_lat())







# max = len(lista[0]["nazwisko"])
# nazwisko = lista[0]["nazwisko"]
# for pacjent in lista:
#     if max < len(pacjent["nazwisko"]):
#         max = len(pacjent["nazwisko"])
#         nazwisko = pacjent["nazwisko"]
#
# print(f"Suma lat wynosi {suma}")
# print(f"Średni wiek wynosi {suma/len(lista):.0f}")
# print(f"Najdłuższe nazwisko: {nazwisko}")
