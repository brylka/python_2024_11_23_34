from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Witaj świecie!"

@app.route('/rates')
def get_rates():
    url = "https://api.frankfurter.dev/v1/latest?base=PLN"

    response = requests.get(url)
    data = response.json()
    base = data['base']
    date = data['date']
    rates = data['rates']
    pln = 100

    text = ''
    for a, b in rates.items():
        text += f"{pln}PLN to: {b:10.4f} \t\t{pln * float(b):10.2f}{a}"
    return text


if __name__ == '__main__':
    app.run(debug=True)
