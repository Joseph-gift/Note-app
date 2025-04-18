from flask import Blueprint

# Defining a blueprint for the website module
views = Blueprint("views", __name__)

# Defining a route for the home page
# This route will be accessible at the root URL ("/")
@views.route("/")
def home():
    return "<h1>Home Page</h1>"