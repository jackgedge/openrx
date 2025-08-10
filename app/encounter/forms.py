from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError
from sqlalchemy.orm import Session
from app.extensions import engine
from app.models import Patient

class PatientEncounterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=40)])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired()])
    patient_id = IntegerField('Patient ID', validators=[InputRequired()])
    submit = SubmitField('Submit')
    pc = StringField('Presenting Complaint', validators=[InputRequired()])
    exam = TextAreaField('Examination', validators=[InputRequired()])
    hpc = TextAreaField('History of Presenting Complaint', validators=[InputRequired()])
    hr = IntegerField('HR', validators=[InputRequired(), NumberRange(min=0, max=300)])
    sbp = IntegerField('SBP', validators=[InputRequired(), NumberRange(min=0, max=300)])
    dbp = IntegerField('DBP', validators=[InputRequired(), NumberRange(min=0, max=200)])
    rr = IntegerField('RR', validators=[InputRequired(), NumberRange(min=0, max=100)])
    temp = DecimalField('Temp', validators=[InputRequired(), NumberRange(min=25, max=45)])
    cbg = DecimalField('CBG', validators=[InputRequired(), NumberRange(min=0, max=60)])
    gcs_e = IntegerField('GCS Eyes', validators=[InputRequired(), NumberRange(min=1, max=4)])
    gcs_v = IntegerField('GCS Verbal', validators=[InputRequired(), NumberRange(min=1, max=5)])
    gcs_m = IntegerField('GCS Motor', validators=[InputRequired(), NumberRange(min=1, max=6)])
    diagnosis_1 = StringField('Diagnosis', validators=[InputRequired()])
    icd_11_1 = StringField('ICD-11')
    tx = StringField('Treatment', validators=[InputRequired()])
    outcome = StringField('Outcome', validators=[InputRequired()])

    def validate_patient_id(self, field):
        with Session(engine) as session:
            patient = session.query(Patient).filter_by(
                id=self.patient_id.data,
                first_name=self.first_name.data,
                last_name=self.last_name.data,
                dob=self.dob.data
            ).first()
            if not patient:
                raise ValidationError("No matching patient found.")