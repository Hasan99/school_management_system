from datetime import datetime
from app import db, ma


# child table
class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    date_of_birth = db.Column(db.Date)
    b_form_cnic = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True)
    registration_date = db.Column(db.DateTime, default=datetime.now)
    person_image = db.Column(db.LargeBinary)
    address_id = db.Column(db.Integer, db.ForeignKey("address.address_id"), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"))
    address = db.relationship("Address", backref="person")
    branch = db.relationship("Branch", backref="person")


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
