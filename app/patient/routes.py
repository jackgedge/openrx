from flask import render_template, request, redirect, url_for
from flask_login import login_required
from app.auth.helpers import *
from app.models import *
from app.patient import patient_bp
from app.patient.forms import *

@patient_bp.route("/register", methods=["GET", "POST"])
@login_required
def register():

    form = PatientRegistrationForm()

    if request.method == "POST":

        if form.validate_on_submit():
            
            first_name = form.first_name.data
            last_name = form.last_name.data
            dob = form.dob.data

            with Session(engine) as session:
                new_patient = Patient(first_name=first_name, last_name=last_name, dob=dob)

                session.add(new_patient)
                session.commit()

            return redirect(url_for('main.home'))
    
    else:
        return render_template("/patient/register.html", form=form, title="Register Patient")
    
@patient_bp.route("/list", methods=["GET", "POST"])
@login_required
def list():

    form = PatientFilterForm(request.form)

    with Session(engine) as session:
        patients_query = session.query(Patient)

        if form.validate_on_submit():
            if form.patient_id.data:
                patients_query = patients_query.filter(Patient.id.ilike(f"%{form.patient_id.data}%"))
            if form.first_name.data:
                patients_query = patients_query.filter(Patient.first_name.ilike(f"%{form.first_name.data}%"))
            if form.last_name.data:
                patients_query = patients_query.filter(Patient.last_name.ilike(f"%{form.last_name.data}%"))
            if form.dob.data:
                patients_query = patients_query.filter(Patient.dob.ilike(f"%{form.dob.data}%"))
            # Add more filters as needed

        patients = patients_query.all()

        return render_template("/patient/list.html", patients=patients, form=form)

        