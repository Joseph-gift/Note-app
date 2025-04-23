from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# Defining a blueprint for the website module
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    data = request.form
    return render_template("login.html",boolean=True)

@auth.route("/logout")
def logout():
    return render_template("home.html")

@auth.route("/signup",  methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get("username")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        if len(email) < 4:
            flash("Your Email is not valid", category="error")
        elif len(username) < 3:
            flash("Your username must be greater than 2 character", category="error")
        elif len(password) < 7:
            flash("Your password is too short", category="error")
        elif password != confirmPassword:
            flash("Your password do not match", category="error")
        else:
            # Create a User
            new_user = User(email=email, username=username,password=generate_password_hash(password, method="pbkdf2:sha256"))
            # Add User to database
            db.session.add(new_user)
            db.session.commit()

            flash("Account created succefully", category="succes")
            return redirect(url_for("views.home"))

    return render_template("signup.html")


