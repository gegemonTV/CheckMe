from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home_page():
    return render_template("home_page/index.html")

@app.route("/usage")
def usage_page():
    return render_template("usage_page/index.html")

@app.route("/start")
def start_page():
    return render_template("start_page/index.html")

@app.route("/login")
def login_page():
    return render_template("login_page/index.html")

@app.route("/sign_up")
def sign_up_page():
    return render_template("sign_up_page/index.html")


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", 8080)