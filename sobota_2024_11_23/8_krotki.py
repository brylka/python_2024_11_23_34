lista = [2, "string", True]
print(lista[1])
lista[1] = "STRING"
print(lista[1])

krotka = (2, "string", True)
print(krotka[1])
krotka.append("Kolejny element")
print(krotka)