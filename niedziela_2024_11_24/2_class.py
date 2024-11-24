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

s1 = Samochod("BMW")
s2 = Samochod("Fiat")
while True:
    ktory = int(input("Który samochów? (1 lub 2): "))
    if ktory == 1:
        co = int(input(f"Co zrobić z samochodem {s1.marka}? (1-przyśpiesz, 2-zwolnij, 3-sprawdż stan): "))
        if co == 1:
            s1.jedz()
        elif co == 2:
            s1.hamuj()
        elif co == 3:
            s1.stan()
    if ktory == 2:
        co = int(input(f"Co zrobić z samochodem {s2.marka}? (1-przyśpiesz, 2-zwolnij, 3-sprawdż stan): "))
        if co == 1:
            s2.jedz()
        elif co == 2:
            s2.hamuj()
        elif co == 3:
            s2.stan()
