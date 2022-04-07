from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route("/")
def index():
    return render_template("index.html", across=4, down=4)


@app.route("/<x>/<y>/")
def play(x, y):
    return render_template("index.html", across=int(x), down=int(y))


if __name__ == "__main__":
    app.run(debug=True)