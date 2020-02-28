from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.routes.student_route import blueprint_student
from app.routes.parent_route import blueprint_parent

app.register_blueprint(blueprint_student)
app.register_blueprint(blueprint_parent)

from app.models import address_model, branch_model, role_model, person_model, parent_model, student_model, user_model, \
    section_model, class_model

db.create_all()
