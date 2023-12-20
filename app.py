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


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, port=8080)  # moæna zmienić port

# 127.0.0.1 - localhost - nasz komputer
