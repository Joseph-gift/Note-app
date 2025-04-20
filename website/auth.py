from flask import Blueprint, render_template, request

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
            pass
        elif len(username) < 2:
            pass
        elif password != confirmPassword:
            pass
        elif len(password) < 7:
            pass
        else:
            # Add User to database
            pass
    return render_template("signup.html")
