from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Simple settings
app.secret_key = "my-simple-secret-key"

# Login information
USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/", methods=["GET"])
def index():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    return redirect(url_for("dashboard"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == USERNAME and password == PASSWORD:

            session["logged_in"] = True

            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="نام کاربری یا رمز عبور اشتباه است."
        )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "logged_in" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=USERNAME
    )


@app.route("/settings")
def settings():

    if "logged_in" not in session:
        return redirect(url_for("login"))

    return render_template(
        "settings.html",
        username=USERNAME
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":

    port = 8080

    app.run(
        host="0.0.0.0",
        port=port
    )
