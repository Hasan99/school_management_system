from main import db, ma


class Branch(db.Model):
    branch_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.relationship("Address", backref="branch", uselist=False)

    def __init__(self, name):
        self.name = name


class BranchSchema(ma.ModelSchema):
    class Meta:
        model = Branch
