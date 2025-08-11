from flask import Blueprint

note_bp = Blueprint("note", __name__, url_prefix="/note")

from app.note import routes