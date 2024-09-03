"""
Defines the Note model for the application.

The Note model represents notes created by users, including their content and associated user.
"""

from ..database import db

class Note(db.Model):
    """
    Represents a note created by a user.

    Attributes:
        id (int): The unique identifier for the note.
        title (str): The title of the note.
        content (str): The content of the note.
        user_id (int): The ID of the user who created the note.
    """
    id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255))  # Ensure this is the correct attribute name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('note', lazy=True))