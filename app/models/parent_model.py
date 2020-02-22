from app import db, ma


# parent table
class Parent(db.Model):
    __tablename__ = "parent"
    parent_id = db.Column(db.Integer, primary_key=True)
    father_guardian = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    parent_cnic = db.Column(db.String(50), nullable=False, unique=True)
    occupation = db.Column(db.String(100), nullable=False)
    income = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)

    # student = db.relationship("Student", back_populates="parent")

    def __init__(self, father_guardian, mother_name, parent_cnic, occupation, income, phone_number):
        self.father_guardian = father_guardian
        self.mother_name = mother_name
        self.parent_cnic = parent_cnic
        self.occupation = occupation
        self.income = income
        self.phone_number = phone_number


class ParentSchema(ma.ModelSchema):
    class Meta:
        model = Parent
