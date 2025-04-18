from flask import Blueprint, render_template

# Defining a blueprint for the website module
views = Blueprint("views", __name__)

# Defining a route for the home page
# This route will be accessible at the root URL ("/")
@views.route("/")
def home():
    return render_template('home.html')