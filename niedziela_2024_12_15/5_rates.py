from flask import Flask, render_template, request
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
    rates = data['rates']

    return render_template("rates.html", a=rates)

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    url = "https://api.frankfurter.dev/v1/latest?base=PLN"
    response = requests.get(url)
    data = response.json()
    rates = data['rates']

    if request.method == 'POST':
        try:
            pln = float(request.form['pln'])
        except:
            pln = 0
        currency = request.form['currency']
        result = rates[currency]*pln
        text = f"Kwota {pln}PLN to {result}{currency} - przelicznik {rates[currency]}"
        return render_template("convert.html", a=rates, text=text)
    else:
        return render_template("convert.html", a=rates)


if __name__ == '__main__':
    app.run(debug=True)
