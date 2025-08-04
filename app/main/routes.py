from flask import render_template, request, redirect, url_for
from flask_login import login_required
from app.auth.helpers import *
from app.models import *
from app.main import main_bp
from app.main.forms import *


@main_bp.route("/")
def index():
    return redirect(url_for("auth.login"))


@main_bp.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("main/home.html", title="Home")


@main_bp.route("/register_patient", methods=["GET", "POST"])
@login_required
def register_patient():

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
        return render_template("/main/register_patient.html", form=form, title="Register Patient")


@main_bp.route("/record_encounter", methods=["GET", "POST"])
@login_required
def record_encounter():

    form = PatientEncounterForm()

    if request.method == 'POST':
        
        if form.validate_on_submit():

            first_name = form.first_name.data
            last_name = form.last_name.data
            dob = form.dob.data
            patient_id = form.patient_id.data
            pc = form.pc.data
            hpc = form.hpc.data
            exam = form.exam.data
            hr = form.hr.data
            sbp = form.sbp.data
            dbp = form.dbp.data
            rr = form.rr.data
            temp = form.temp.data
            cbg = form.cbg.data
            gcs_e = form.gcs_e.data
            gcs_v = form.gcs_v.data
            gcs_m = form.gcs_m.data
            diagnosis_1 = form.diagnosis_1.data
            icd_11_1 = form.icd_11_1.data
            tx = form.tx.data
            outcome = form.tx.data

            # Look-Up Patient ID


            # Submit encounter
            with Session(engine) as session:
                new_encounter = Encounter(
                    pc=pc,
                    hpc=hpc,
                    exam=exam,
                    hr=hr,
                    sbp=sbp, 
                    dbp=dbp,
                    rr=rr,
                    temp=temp,
                    cbg=cbg,
                    gcs_e=gcs_e, 
                    gcs_v=gcs_v, 
                    gcs_m=gcs_m,
                    diagnosis_1=diagnosis_1,
                    icd_11_1=icd_11_1,
                    tx=tx,
                    outcome=outcome
                )
        
                session.add(new_encounter)
                session.commit()

            return redirect(url_for('main.home'))
        return render_template("/main/record_encounter.html", form=form, title="Record Encounter")
    
    else: 
                return render_template("/main/record_encounter.html", form=form, title="Record Encounter")
    

@main_bp.route("/patients", methods=["GET", "POST"])
@login_required
def patients():
    with Session(engine) as session:
        patients = session.query(Patient).all()
        return render_template("/main/patients.html", patients=patients)
    

@main_bp.route("/encounters", methods=["GET", "POST"])
@login_required
def encounters():
     with Session(engine) as session:
          encounters = session.query(Encounter).all()
          return render_template("/main/encounters.html", encounters=encounters)