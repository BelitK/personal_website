from flask import Flask, render_template, Response, request, redirect, url_for


# instatiate flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Homepage.html")


@app.route("/kommunity")
def kommunity():
    return render_template("Kommunity.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="8000")
