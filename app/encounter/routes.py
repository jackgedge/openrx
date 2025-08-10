from flask import render_template, request, redirect, url_for
from flask_login import logout_user, login_required, login_user
from werkzeug.security import generate_password_hash
from app.auth.helpers import *
from .forms import *
from app.models import *
from app.encounter import encounter_bp

@encounter_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():

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

            

            # Submit encounter
            with Session(engine) as session:

                new_encounter = Encounter(
                    patient_id=patient_id,
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
        
                patient = session.query(Patient).filter_by(id=patient_id).first()
                if not patient:
                    return raise_error(403, "Invalid patient")
                else: 
                    session.add(new_encounter)
                    session.commit()

            return redirect(url_for('main.home'))
        return render_template("/encounter/new.html", form=form, title="Record Encounter")
    
    else: 
        return render_template("/encounter/new.html", form=form, title="Record Encounter")
    
    

@encounter_bp.route("/list", methods=["GET", "POST"])
@login_required
def list():
     with Session(engine) as session:
          encounters = session.query(Encounter).all()
          return render_template("/encounter/list.html", encounters=encounters)