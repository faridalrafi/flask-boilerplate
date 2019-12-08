from flask import Blueprint, jsonify
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import current_user, jwt_required, jwt_optional
import os
import json
blueprint = Blueprint('root', __name__)


@blueprint.route('/api/', methods=('GET',))
@jwt_optional
def get_root():
    res = "TEST API OK"
    return res

@blueprint.route('/swagger', methods=('GET',))
def get_swagger():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'swagger.json')
    with open(my_file)as f:
        d = json.load(f)
    return d
