lista = [
    {"imie": "Bartosz", "nazwisko": "Bryniarski", "wiek": 45, "adres": "Jelenia Góra"},
    {"imie": "Adam", "nazwisko": "Małysz", "wiek": 50, "adres": "Wisła"},
    {"imie": "Albert", "nazwisko": "Kwas", "wiek": 18, "adres": "Wrocław"}
]

suma = 0
for pacjent in lista:
    suma += pacjent['wiek']
    print(pacjent['nazwisko'])
print(f"Suma lat wynosi {suma}")
print(f"Średni wiek wynosi {suma/len(lista):.0f}")