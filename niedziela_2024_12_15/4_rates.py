import requests


url = "https://api.frankfurter.dev/v1/latest?base=PLN"

response = requests.get(url)
data = response.json()
base = data['base']
date = data['date']
rates = data['rates']

#print(base, date, rates['EUR'])
pln = float(input("Podaj kowotę w PLN: "))
print(f"Kwota {pln}PLN to {pln*float(rates['EUR'])}EURO")