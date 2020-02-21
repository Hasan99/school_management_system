from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.routes.student_route import blueprint_student

app.register_blueprint(blueprint_student)

from app.models import address_model, branch_model, parent_model, role_model, person_model, student_model, user_model, \
    contact_model, section_model, class_model

# from app.models import models

db.create_all()
print("db.create_all() called")
