from flask import jsonify, request, Blueprint
from schema_definition import parent_schema
from cerberus import Validator

blueprint_parent = Blueprint("blueprint_parent", __name__)


@blueprint_parent.route("/parent", methods=["POST"])
def add_parent():
    validator = Validator(parent_schema)
    data = request.get_json()
    is_valid = validator.validate(data)
    if is_valid:
        print("in if")
        return jsonify({"result": "parent already registered"})
    else:
        print("in else")
        return jsonify(validator.errors)
