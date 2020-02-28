from flask import jsonify, request, Blueprint
from schema_definition import parent_schema
from cerberus import Validator

blueprint_parent = Blueprint("blueprint_parent", __name__)


def insert_parent(data, has_email, has_image):
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
            address = Address(data["home_address"], data["city"], data["province_state"],
                              data["country"])
            person = Person(person_name=data["person_name"], b_form_cnic=data["b_form_cnic"],
                            phone_number=data["phone_number"], email=data["email"],
                            person_image=image_in_bytes if has_image else None, person=address,
                            branch_id=data["branch_id"])
            parent = Parent(mother_name=data["mother_name"], occupation=data["occupation"],
                            parent=person)

            db.session.add(address)
            db.session.add(person)
            db.session.add(parent)
            db.session.commit()

            parent_schema_ = ParentSchema()
            return jsonify(parent_schema_.dump(parent))


@blueprint_parent.route("/parent", methods=["POST"])
def add_parent():
    validator = Validator(parent_schema)
    data = request.get_json()
    is_valid = validator.validate(data)

    if is_valid:
        print("in if")
        print("data:", data)
        from app.models.person_model import Person

        person_obj = Person.query.filter_by(b_form_cnic=data["b_form_cnic"]).first()

        if person_obj:
            return jsonify({"result": f"'{data['b_form_cnic']}' already exists"})
        else:
            person_obj = Person.query.filter_by(phone_number=data["phone_number"]).first()

            if person_obj:
                return jsonify({"result": f"'{data['phone_number']}' already exists"})
            else:
                has_email = False
                has_image = False

                if data["email"]:
                    has_email = True
                    person_obj = Person.query.filter_by(email=data["email"]).first()

                    if person_obj:
                        return jsonify({"result": f"'{data['email']}' already exists"})
                    else:
                        insert_parent(data, has_email, has_image)
                else:
                    insert_parent(data, has_email, has_image)
    else:
        return jsonify(validator.errors)
