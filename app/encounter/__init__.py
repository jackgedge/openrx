from flask import Blueprint

encounter_bp = Blueprint("encounter", __name__, url_prefix="/encounter")

from app.encounter import routes