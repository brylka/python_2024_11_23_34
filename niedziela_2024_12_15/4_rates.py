import requests

url = "https://api.frankfurter.dev/v1/latest?base=PLN"

response = requests.get(url)
data = response.json()
base = data['base']
date = data['date']
rates = data['rates']

#print(base, date, rates['EUR'])
pln = float(input("Podaj kowotę w PLN: "))
#print(f"Kwota {pln}PLN to {pln*float(rates['EUR'])}EURO")

for a, b in rates.items():
    print(f"{pln}PLN to: {b:10.4f} \t\t{pln*float(b):10.2f}{a}")
