from app import db, ma


# child table
class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"), nullable=False)
    role = db.relationship("Role", backref="user")


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
