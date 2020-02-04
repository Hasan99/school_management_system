if __name__ == '__main__':
    from main import db, ma


# child table
class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), nullable=False, unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"))
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("parent.parent_id"))


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
