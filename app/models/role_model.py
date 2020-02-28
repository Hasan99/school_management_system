from app import db, ma


# parent table
class Role(db.Model):
    __tablename__ = "role"
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role
