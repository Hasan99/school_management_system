if __name__ == '__main__':
    from main import db, ma


# parent table
class Branch(db.Model):
    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(200), nullable=False)
    address = db.relationship("Address", backref="branch", uselist=False)

    def __init__(self, branch_name):
        self.branch_name = branch_name


class BranchSchema(ma.ModelSchema):
    class Meta:
        model = Branch
