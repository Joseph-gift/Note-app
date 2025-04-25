from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# Defining a blueprint for the website module
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the email and password are correct
        # If the email and password are correct, log the user in
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfuly", category = "success")
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password", category="error")
        else:
            flash("Email does not exist.", category="error")
    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/signup",  methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get("username")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        # Make sure the email is not already in the database
        user = User.query.filter_by(email=email).first()
        if user:
            flash("email already in exit", category="error")

        if len(email) < 4:
            flash("Your Email is not valid", category="error")
        elif User.query.filter_by(username=username).first():
            flash("Username already exit.",category="error")
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
            login_user(user,remember=True)

            flash("Account created succefully", category="succes")
            return redirect(url_for("views.home"))

    return render_template("signup.html",user=current_user)


