from flask import Blueprint, render_template
from flask_login import  login_required, current_user


# Defining a blueprint for the website module
views = Blueprint("views", __name__)

# Defining a route for the home page
# This route will be accessible at the root URL ("/")
@views.route("/")
@login_required
def home():
    return render_template('home.html', user=current_user)