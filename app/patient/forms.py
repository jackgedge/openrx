from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, EqualTo, NumberRange, ValidationError, Optional
from sqlalchemy.orm import Session
from app.extensions import engine
from app.models import Patient

class PatientRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=40)])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired()])
    submit = SubmitField('Register')

class PatientFilterForm(FlaskForm):
    patient_id = IntegerField('Patient ID', validators=[Optional()])
    first_name = StringField('First Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[Optional()])
    dob = DateField('DOB', validators=[Optional()])
    submit = SubmitField('Filter')