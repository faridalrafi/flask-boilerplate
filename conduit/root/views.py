from flask import Blueprint, jsonify
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import current_user, jwt_required, jwt_optional
blueprint = Blueprint('root', __name__)


@blueprint.route('/api/', methods=('GET',))
@jwt_optional
def get_root():
    res = "TEST API OK"
    return res
