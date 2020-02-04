if __name__ == '__main__':
    from main import db, ma


# child table
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"))


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
