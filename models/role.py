from main import db, ma


class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship("User", backref="role")

    def __init__(self, name):
        self.name = name


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role
