from flask import Flask

# Creating a flask application instance
# This is the entry point for the Flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecret_key'

    # Registering the blueprints for the website module
    from .views import views
    from .auth import auth

    # Registering the blueprints with the application instance
    # The views blueprint will handle the routes for the main website functionality
    # The auth blueprint will handle the routes for authentication functionality
    # The url_prefix argument specifies the URL prefix for each blueprint
    # For example, all routes in the auth blueprint will be prefixed with "/auth"
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app