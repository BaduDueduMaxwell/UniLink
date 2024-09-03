"""
Initializes the Flask application, sets up database, and configures login manager.
"""

from flask import Flask
from os import path
from flask_login import LoginManager
from .database import db

DB_NAME = "database.db"

def create_app():
    """
    Creates and configures the Flask application.
    
    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dkfdkfndf@'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """
        Loads a user by their ID.
        
        Args:
            id (int): The user's ID.

        Returns:
            User: The User object corresponding to the ID.
        """
        return User.query.get(int(id))

    return app

def create_database(app):
    """
    Creates the database if it does not already exist.
    
    Args:
        app (Flask): The Flask application instance.
    """
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
