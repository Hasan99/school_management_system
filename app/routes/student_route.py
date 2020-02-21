from flask import jsonify, request, Blueprint
from schema_definition import student_schema
from cerberus import Validator

blueprint_student = Blueprint("blueprint_student", __name__)


@blueprint_student.route("/student", methods=["POST"])
def add_student():
    validator = Validator(student_schema)
    data = request.get_json()
    is_valid = validator.validate(data)
    # from models import student_model
    if is_valid:
        print("data valid hai .. data nikaaL kr database main store krna hai ..")
        print(data)
        # roll_number = data["roll_number"]
        count = 5
        if count > 0:
            return jsonify({"result": f"roll_number '{count}' already exists"})
        else:
            print("in else")
            return jsonify({"result": "student added successfully"})
    else:
        return jsonify(validator.errors)
