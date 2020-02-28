from app import db, ma


# child table
class Parent(db.Model):
    __tablename__ = "parent"
    parent_id = db.Column(db.Integer, primary_key=True)
    mother_name = db.Column(db.String(100))
    occupation = db.Column(db.String(100), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    person = db.relationship("Person", backref="parent")


class ParentSchema(ma.ModelSchema):
    class Meta:
        model = Parent
