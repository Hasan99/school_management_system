from main import db, ma


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"))


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
