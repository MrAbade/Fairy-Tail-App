from flask import Blueprint


bp_sorcerer = Blueprint('bp_sorcerer', __name__)

@bp_sorcerer.route('/')
def list_all():
    ...
