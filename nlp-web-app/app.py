from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_registration", methods=["POST"])
def perform_registration():
    name = request.form.get("user_ka_name")
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")

    response = dbo.insert(name, email, password)

    if response:
        return render_template("login.html", message="Registration succesful!. Kindly login to proceed")
    else:
        return render_template("register.html", message="Email already exists")
    

@app.route("/perform_login", methods=["POST"])
def perform_login():
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")

    response = dbo.search(email, password)

    if response:
        return redirect("/profile")
    else:
        return render_template("login.html", message="Incorrect email/password")

@app.route("/profile")
def profile():
    return "Profile"


app.run(debug = True)