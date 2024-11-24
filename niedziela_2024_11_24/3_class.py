class Samochod:
    def __init__(self,marka):
        self.marka = marka
        self.predkosc = 0
        self.sprawny = True
    def stan(self):
        print(f"Prędkość samochodu {self.marka} wynosi {self.predkosc}km/h.")
    def jedz(self):
        self.predkosc += 10
        print(f"Samochód {self.marka} jedzie z prędkością {self.predkosc}km/h.")
    def hamuj(self):
        self.predkosc -= 10
        print(f"Samochód {self.marka} hamuje i jedzie z prędkością {self.predkosc}km/h.")

samochody = [Samochod("BMW"), Samochod("Fiat")]

while True:
    ktory = int(input("Który samochód? (0 lub 1): "))
    co = int(input(f"Co zrobić z samochodem {samochody[ktory].marka}? (1-przyśpiesz, 2-zwolnij, 3-sprawdż stan): "))
    if co == 1:
        samochody[ktory].jedz()
    elif co == 2:
        samochody[ktory].hamuj()
    elif co == 3:
        samochody[ktory].stan()

