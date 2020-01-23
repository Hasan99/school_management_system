from main import app
from flask import jsonify, request


@app.route("/student", methods=["POST"])
def add_student():
    data = request.get_json()
    if data is not None:
        pass
# return jsonify({"response": "added"})
