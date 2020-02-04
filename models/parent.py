if __name__ == '__main__':
    from main import db, ma


# parent table
class Parent(db.Model):
    parent_id = db.Column(db.Integer, primary_key=True)
    father_guardian = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    income = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)
    children = db.relationship("Student", backref="parent")

    def __init__(self, father_guardian, mother_name, occupation, income, phone_number):
        self.father_guardian = father_guardian
        self.mother_name = mother_name
        self.occupation = occupation
        self.income = income
        self.phone_number = phone_number


class ParentSchema(ma.ModelSchema):
    class Meta:
        model = Parent
