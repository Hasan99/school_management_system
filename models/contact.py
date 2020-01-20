from main import db, ma


class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"))


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = Contact
