from flask import Flask, render_template, request

import server

template_folder = "../templates/"

app = Flask(__name__, template_folder=template_folder)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return server.login()

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
