from flask import jsonify, request, Blueprint
from schema_definition import student_schema
from cerberus import Validator

blueprint_student = Blueprint("blueprint_student", __name__)


@blueprint_student.route("/student", methods=["POST"])
def add_student():
    validator = Validator(student_schema)
    data = request.get_json()
    is_valid = validator.validate(data)
    from app.models.person_model import Person, db
    from app.models.address_model import Address
    if is_valid:
        print("Received JSON:\n", data)
        b_form_cnic = data["b_form_cnic"]
        row = Person.query.filter_by(b_form_cnic=b_form_cnic).first()
        print("row value:", row, "\ntype of row:", type(row))
        if row is not None:
            return jsonify({"result": "b_form_cnic already exists"})
        else:
            print("in else")
            address_obj = Address(data["home_address"], data["city"], data["province_state"], data["country"])

            db.session.add(address_obj)
            db.session.commit()
            return jsonify({"result": "student added successfully"})
    else:
        return jsonify(validator.errors)
