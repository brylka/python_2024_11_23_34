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
    rates = data['rates']

    return render_template("rates.html", a=rates)


if __name__ == '__main__':
    app.run(debug=True)
