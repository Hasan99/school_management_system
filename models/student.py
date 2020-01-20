from main import db, ma


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(50), nullable=False, unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"))
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("parent.parent_id"))


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
