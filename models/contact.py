if __name__ == '__main__':
    from main import db, ma


# child table
class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), default="not available")
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"))


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = Contact
