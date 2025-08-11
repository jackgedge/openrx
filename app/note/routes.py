from flask import render_template, request, redirect, url_for
from flask_login import login_required
from app.auth.helpers import *
from app.models import *
from app.note import note_bp
from app.note.forms import *

@note_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = NoteForm()

    if request.method == "POST":
        patient_id = form.patient_id.data
        note = form.note.data
        author = form.author.data
        return render_template("/note/new.html", form=form)
    else:
        return render_template("/note/new.html")