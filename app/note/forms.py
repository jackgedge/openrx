from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError, Optional
from sqlalchemy.orm import Session

from app.extensions import *
from app.models import *

class NoteForm(FlaskForm):
    note = TextAreaField("Note", validators=[InputRequired()])
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    submit = SubmitField("Save")
