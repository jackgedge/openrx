from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError, Optional
from sqlalchemy.orm import Session

from app.extensions import *
from app.models import *

class NoteForm(FlaskForm):
    patient_id = IntegerField("Patient ID", validators=[InputRequired()])
    note = TextAreaField("Note", validators=[InputRequired()])
    author = IntegerField("Author", validators=[InputRequired()])
    submit = SubmitField("Save")
