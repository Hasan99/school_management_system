from app import db, ma

class_section = db.Table("class_section",
                         db.Column("class_id", db.Integer, db.ForeignKey("class.class_id"), nullable=False),
                         db.Column("section_id", db.Integer, db.ForeignKey("section.section_id"), nullable=False),
                         db.Column("student_id", db.Integer, db.ForeignKey("student.student_id"), nullable=False),
                         db.Column("year_of_passing", db.String(30))
                         )


# parent table
class Class(db.Model):
    __tablename__ = "class"
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    section = db.relationship("Section", secondary=class_section, backref="Class")

    def __init__(self, class_name):
        self.class_name = class_name


class ClassSchema(ma.ModelSchema):
    class Meta:
        model = Class
