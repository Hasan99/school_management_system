from flask import jsonify, request, Blueprint
from schema_definition import parent_schema
from cerberus import Validator

blueprint_parent = Blueprint("blueprint_parent", __name__)


def insert_parent(parent_data, has_email, has_image):
    from app.models.parent_model import Parent, db, ParentSchema
    from app.models.person_model import Person
    from app.models.address_model import Address

    two_mb = 2097152  # number of bytes
    image_file = request.files["person_image"]
    image_in_bytes = image_file.read()
    image_size_in_bytes = len(image_in_bytes)

    if image_size_in_bytes == 0:
        has_image = False
    else:
        has_image = True

        if image_size_in_bytes > two_mb:
            return jsonify({"result": "image size is greater than 2 MB"})
        else:
            address = Address(parent_data["home_address"].lower(), parent_data["city"].lower(),
                              parent_data["province_state"].lower(),
                              parent_data["country"].lower())
            person = Person(person_name=parent_data["person_name"].lower(), b_form_cnic=parent_data["b_form_cnic"],
                            phone_number=parent_data["phone_number"], email=parent_data["email"].lower(),
                            person_image=image_in_bytes if has_image else None, branch_id=int(parent_data["branch_id"]))
            parent = Parent(mother_name=parent_data["mother_name"].lower(),
                            occupation=parent_data["occupation"].lower())

            address.persons.append(person)
            person.parents.append(parent)

            db.session.add(address)
            db.session.add(person)
            db.session.add(parent)
            db.session.commit()

            parent_schema_object = ParentSchema()
            response = parent_schema_object.dump(parent)
            return response


@blueprint_parent.route("/parent", methods=["POST"])
def add_parent():
    validator = Validator(parent_schema)
    parent_data = {
        "home_address": request.form["home_address"],
        "city": request.form["city"],
        "province_state": request.form["province_state"],
        "country": request.form["country"],

        "person_name": request.form["person_name"],
        "b_form_cnic": request.form["b_form_cnic"],
        "phone_number": request.form["phone_number"],
        "email": request.form["email"],

        "branch_id": request.form["branch_id"],

        "mother_name": request.form["mother_name"],
        "occupation": request.form["occupation"]
    }

    is_valid = validator.validate(parent_data)

    if is_valid:
        from app.models.person_model import Person

        person_row = Person.query.filter_by(b_form_cnic=parent_data["b_form_cnic"]).first()

        if person_row:
            return jsonify({"result": f"'{parent_data['b_form_cnic']}' already exists"})
        else:
            person_row = Person.query.filter_by(phone_number=parent_data["phone_number"]).first()

            if person_row:
                return jsonify({"result": f"'{parent_data['phone_number']}' already exists"})
            else:
                has_email = False
                has_image = False

                if parent_data["email"]:
                    has_email = True
                    person_row = Person.query.filter_by(email=parent_data["email"]).first()

                    if person_row:
                        return jsonify({"result": f"'{parent_data['email']}' already exists"})
                    else:
                        response = insert_parent(parent_data, has_email, has_image)
                        return jsonify(response)
                else:
                    response = insert_parent(parent_data, has_email, has_image)
                    return jsonify(response)
    else:
        return jsonify(validator.errors)
