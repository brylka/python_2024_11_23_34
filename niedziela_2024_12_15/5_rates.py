from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/rates')
def get_rates():
    url = "https://api.frankfurter.dev/v1/latest?base=PLN"

    response = requests.get(url)
    data = response.json()
    # base = data['base']
    # date = data['date']
    rates = data['rates']
    # pln = 100

    # text = ''
    # for a, b in rates.items():
    #     text += f"{pln}PLN to: {b:10.4f} \t\t{pln * float(b):10.2f}{a}<br>"
    return render_template("rates.html", a=rates)


if __name__ == '__main__':
    app.run(debug=True)
