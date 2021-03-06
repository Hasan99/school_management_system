from app import db, ma


# child table
class Contact(db.Model):
    __tablename__ = "contact"
    contact_id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    person = db.relationship("Person", backref="contacts")


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = Contact
