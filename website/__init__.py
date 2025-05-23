from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initializing the SQLAlchemy object
# This object will be used to interact with the database
db = SQLAlchemy()
DB_NAME = "database.db"

# Creating a flask application instance
# This is the entry point for the Flask application
def create_app():
    '''
     Creating a Flask application instance
     The __name__ argument is used to determine the root path of the application
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecret_key'
    # Setting the configuration for the SQLAlchemy database URI
    # The database URI specifies the type of database and its location
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    
    # Initializing the database with the application instance
    db.init_app(app)


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

    from .models import User, Note

    with app.app_context():
        db.create_all()

    # Initialize the LoginManager
    # This object will be used to manage user sessions and authentication
    # The login_view attribute specifies the view function to redirect to when a user is not logged in
    # In this case, it will redirect to the "auth.login" view function
    # The login_manager.init_app(app) method initializes the LoginManager with the application instance
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # Load the user by it Id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
