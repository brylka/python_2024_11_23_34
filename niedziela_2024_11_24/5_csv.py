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

    def srednia_wieku(self):
        return int(self.suma_lat()/len(self.lista))

    def najdluzsze_nazwisko(self):
        max = len(self.lista[0]["nazwisko"])
        nazwisko = self.lista[0]["nazwisko"]
        for pacjent in self.lista:
            if max < len(pacjent["nazwisko"]):
                max = len(pacjent["nazwisko"])
                nazwisko = pacjent["nazwisko"]
        return nazwisko


dane = Dane()
dane.pobierz_dane_z_csv("dane.csv")
print(f"Średnia wieku wynosi: {dane.srednia_wieku()}")
print(f"Najdłuższe nazwisko to: {dane.najdluzsze_nazwisko()}")







#
# print(f"Najdłuższe nazwisko: {nazwisko}")
