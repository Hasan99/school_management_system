from datetime import datetime

if __name__ == '__main__':
    from main import db, ma


# child table
class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    b_form_cnic = db.Column(db.String(50), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)
    address_id = db.Column(db.Integer, db.ForeignKey("address.address_id"))
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"))


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
