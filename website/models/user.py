"""
Defines the User model for the application.

The User model represents a user in the system, including their authentication details and associated notes.
"""

from ..database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    """
    Represents a user in the application.

    Attributes:
        id (int): The unique identifier for the user.
        email (str): The user's email address (must be unique).
        password (str): The hashed password for the user.
        first_name (str): The user's first name.
        notes (relationship): One-to-many relationship to the Note model.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note', backref='author', lazy=True)

    def set_password(self, password):
        """
        Sets the user's password, hashing it before storage.
        """
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        """
        Checks if the provided password matches the stored hashed password.
        
        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password, password)
