from flask import jsonify, request, Blueprint

if __name__ == '__main__':
    from models.address import Address

blueprint_student = Blueprint("blueprint_student", __name__)


@blueprint_student.route("/student", methods=["POST"])
def add_student():
    data = request.get_json()
    print(data)
    return jsonify({"result": "student added successfully"})
