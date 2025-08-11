from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.auth.helpers import *
from app.models import *
from app.note import note_bp
from app.note.forms import *

@note_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = NoteForm()
    patient_id = request.args.get('patient_id')

    if not patient_id:
        return raise_error(404, 'Invalid Patient ID.')

    with Session(engine) as session:
        patient = session.query(Patient).filter_by(id=patient_id).first()
        user = current_user

        if form.validate_on_submit():
            note_text = form.note.data

            new_note = Note(
                patient_id=patient_id,
                note=note_text,
                author_id=current_user.id
            )
            session.add(new_note)
            session.commit()

            return redirect(url_for('patient.view', id=patient_id))

        return render_template("/note/new.html", form=form, patient=patient, user=user, id=patient_id)
        