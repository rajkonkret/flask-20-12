from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    print(request.query_string)

    for p in request.args:
        print(p, request.args[p])

    color = 'black'
    if 'color' in request.args:
        color = request.args['color']

    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    return f'<h1 style="color: {color};font-style: {style}">Hallo World!!!</h1>'


@app.route("/about")
def about():
    a = 10
    b = 1
    return f"<h1>We are programmers {a / b}<h1>"


# /cantor/usd/30
@app.route('/cantor/<currency>/<int:amount>')
def cantor(currency, amount):
    message = f"<h1>You selected {currency} and {amount}<h1>"
    return message


@app.route("/exchange")
def exchange():
    body = f'''
    <form id="exchange_form" action="/exchange_process" method="POST">
        <label for="currency">Currency</label>
        <input type="text" id="currency" name="currency" value="EUR"><br>
        <label for="currency">Amount</label>
        <input type="text" id="amount" name="amount" value="100"><br>
        <input type="submit" value="Send">
    </form>
    '''
    return body
    # body = f"You want to exchange {amount} {currency}"


@app.route('/exchange_process', methods=['POST'])
def exchange_process():
    currency = 'EUR'
    if 'currency' in request.form:
        currency = request.form['currency']

    amount = 100
    if 'amount' in request.form:
        amount = request.form['amount']

    body = f"You want to exchange {amount} {currency}"
    return body


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, port=8080)  # moæna zmienić port

# 127.0.0.1 - localhost - nasz komputer
