from datetime import date

class Samochod:
    def __init__(self, marka, model, kolor, rocznik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        if rocznik < 1970 or rocznik > date.today().year:
            print("Błędna data.")
        else:
            self.rocznik = rocznik
            print(f"Rocznik zmieniony, aktualny to {self.rocznik}.")
    def jedz(self):
        print(f"Samochód {self.marka} {self.model} {self.kolor} {self.rocznik} jedzie.")
    def zmiana_marki(self, nowa_marka):
        self.marka = nowa_marka
    def jaka_marka(self):
        return self.marka
    def zmiana_rocznika(self, nowy_rocznik):
        if nowy_rocznik < 1970 or nowy_rocznik > date.today().year:
            print("Błędna data.")
        else:
            self.rocznik = nowy_rocznik
            print(f"Rocznik zmieniony, aktualny to {self.rocznik}.")


samochod_czerwony = Samochod("Fiat", "126p","czerwony", 1980)
samochod_czerwony.jedz()
#samochod_czerwony.rocznik = -80
samochod_czerwony.zmiana_rocznika(1999)
samochod_czerwony.jedz()










#samochod_czerwony.jedz()
#samochod_niebieski = Samochod("BMW","e30","niebieski", 2000)
#samochod_niebieski.jedz()
#print(samochod_niebieski.marka)
#samochod_niebieski.marka = "Peugeot"
#samochod_niebieski.zmiana_marki("Renault")
#samochod_niebieski.jedz()
#print(samochod_niebieski.jaka_marka())


