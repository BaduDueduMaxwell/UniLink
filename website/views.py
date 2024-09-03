from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models.note import Note
# from .models.university import University
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """
    Renders the home page and handles note creation.

    If the request method is POST, it retrieves the note from the form data,
    validates its length, and adds it to the database if valid. If the note
    is too short, an error message is flashed.

    Returns:
        A rendered template of the home page with the current user's data.
    """
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is too short", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    """
    Deletes a note based on the note ID provided in the request data.

    The note is only deleted if it belongs to the currently logged-in user.

    Returns:
        A JSON response indicating the status of the deletion.
    """
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

# @views.route('/search', methods=['GET'])
# def search():
#     """
#     Handles university search based on query parameters.

#     Retrieves universities from the database that match the search criteria
#     and renders a template with the search results.

#     Returns:
#         A rendered template showing the search results.
#     """
#     query = request.args.get('query', '')
#     universities = University.query.filter(University.name.ilike(f'%{query}%')).all()
#     return render_template("search_results.html", universities=universities)