from flask import Blueprint, render_template

# Defining a blueprint for the website module
auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html",boolean=True)

@auth.route("/logout")
def logout():
    return render_template("home.html")

@auth.route("/signup")
def signup():
    return render_template("signup.html")
