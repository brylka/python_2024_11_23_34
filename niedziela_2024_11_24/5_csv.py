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
while True:
    co = int(input("Co chcesz zrobić? (1-wczytaj dane, 2-podaj średnią, 3-najdłuższe nazwisko): "))
    if co == 1:
        skad = input("Podaj pnazwę pliku (dane na pewno znajdziesz w pliku 'dane.csv'): ")
        dane.pobierz_dane_z_csv(skad)
    elif co == 2:
        print(f"Średnia wieku wynosi: {dane.srednia_wieku()}")
    elif co == 3:
        print(f"Najdłuższe nazwisko to: {dane.najdluzsze_nazwisko()}")

