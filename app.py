from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>Hallo World!!!</h1>"


@app.route("/about")
def about():
    a = 10
    b = 1
    return f"<h1>We are programmers {a / b}<h1>"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, port=8080)  # moæna zmienić port

# 127.0.0.1 - localhost - nasz komputer
