from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import  login_required, current_user
from .models import Note
from .import db
import json


# Defining a blueprint for the website module
views = Blueprint("views", __name__)

# Defining a route for the home page
# This route will be accessible at the root URL ("/")
@views.route("/", methods=["GET","POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if not note or note.strip() == "":
            flash("Your note can't be empty", category="error")
        elif len(note) < 1:
            flash("Your Note is too short! ", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added successfully!", category="success")

    return render_template('home.html', user=current_user)

@views.route("/delete-note", methods=["POST"])
def delete_note():
    # Take data from POST and loaded as json object
    note = json.loads(request.data)
    # Accsess noteId attribute
    noteId = note["noteId"]
    # Look for the note that has that id
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash("Note deleted successfully!", category="success")
    return jsonify({})