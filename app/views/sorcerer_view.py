from flask import Blueprint, jsonify

from ..models.sorcerer import Sorcerer


bp_sorcerer = Blueprint('bp_sorcerer', __name__)

@bp_sorcerer.route('/')
def list_all():
    sorcerer_list = Sorcerer.query.all()

    return jsonify([
        {'name': sorcerer.name}
        for sorcerer in sorcerer_list
    ]), 200
