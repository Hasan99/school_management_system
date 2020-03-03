from app import db, ma


# child table
class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), nullable=False, unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("parent.parent_id"), nullable=False)
    person = db.relationship("Person", backref="students")
    branch = db.relationship("Branch", backref="students")
    parent = db.relationship("Parent", backref="students")


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
