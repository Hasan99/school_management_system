from main import db, ma
from datetime import datetime


class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    b_form_cnic = db.Column(db.String(50), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)
    address_id = db.Column(db.Integer, db.ForeignKey("address.address_id"))
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"))


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
