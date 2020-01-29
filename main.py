from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from routes.student import blueprint_student

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:hasan@localhost/schoolmanagementsystemdb"

app.register_blueprint(blueprint_student)

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"result": "index_route"})


if __name__ == '__main__':
    app.run(debug=True)
