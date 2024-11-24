#lista = [2,"słowo", False, [3,'tak']]
#print(lista[3][1])
slownik = {
    "imie": "Albert",
    "nazwisko": "Kowalski",
    "wiek": 50
}
print(slownik["imie"])
slownik["imie"] = "Krzysztof"
print(slownik["imie"])
print("Klucze", slownik.keys())
for klucz in slownik.keys():
    print(klucz, ":", slownik[klucz])
print(slownik.values())
print(slownik.items())
print(slownik.get("adres","Nie ma takiego klucza"))
slownik.clear()
print(slownik)
