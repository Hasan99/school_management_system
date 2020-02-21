from app import db, ma


# parent table
class Branch(db.Model):
    __tablename__ = "branch"
    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(200), nullable=False)

    # address = db.relationship("Address", back_populates="branch", uselist=False)
    # person = db.relationship("Person", back_populates="branch")

    def __init__(self, branch_name):
        self.branch_name = branch_name


class BranchSchema(ma.ModelSchema):
    class Meta:
        model = Branch
