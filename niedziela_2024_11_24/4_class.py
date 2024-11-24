class Samochod:
    def __init__(self,marka):
        self.marka = marka
        self.predkosc = 0
        self.sprawny = True
    def stan(self):
        if self.sprawny:
            print(f"Prędkość samochodu {self.marka} wynosi {self.predkosc}km/h.")
        else:
            print(f"Samochód {self.marka} jest niesprawny.")
    def jedz(self):
        if self.sprawny:
            self.predkosc += 10
            print(f"Samochód {self.marka} jedzie z prędkością {self.predkosc}km/h.")
    def hamuj(self):
        if self.sprawny:
            self.predkosc -= 10
            print(f"Samochód {self.marka} hamuje i jedzie z prędkością {self.predkosc}km/h.")
    def kolizja(self, inny_samochod):
        if self.sprawny:
            self.sprawny = False
            self.predkosc = 0
            swiat.samochody[inny_samochod].sprawny = False
            swiat.samochody[inny_samochod].predkosc = 0
            print(f"Nastąpiła kolizja {self.marka} z {swiat.samochody[inny_samochod].marka}")

class Swiat:
    def __init__(self):
        self.samochody = []
    def zycie(self):
        while True:
            if len(self.samochody) != 0:
                ktory = int(input(f"Który samochód? (0 - {len(self.samochody)-1}): "))
                co = int(input(f"Co zrobić z samochodem {self.samochody[ktory].marka}? (1-przyśpiesz, 2-zwolnij, 3-sprawdż stan, 4 - kolizja): "))
                if co == 1:
                    self.samochody[ktory].jedz()
                elif co == 2:
                    self.samochody[ktory].hamuj()
                elif co == 3:
                    self.samochody[ktory].stan()
                elif co == 4:
                    inny = int(input(f"Z którym samochodem kolizja? (0 - {len(self.samochody)-1}): "))
                    self.samochody[ktory].kolizja(inny)
            else:
                print("Brak samochodów do zabawy, podaj dane nowego samochodu.")
                ile = int(input("Ile samochodów dodać: "))
                for i in range(ile):
                    marka = input(f"Podaj markę samochodu nr {i}: ")
                    self.samochody.append(Samochod(marka))
                for samochod in self.samochody:
                    print(samochod.marka)

if __name__ == "__main__":
    swiat = Swiat()
    swiat.zycie()
