from main import db, ma

class_section = db.Table("class_section",
                         db.Column("class_id", db.Integer, db.ForeignKey("class.class_id")),
                         db.Column("section_id", db.Integer, db.ForeignKey("section.section_id"))
                         )


class Class(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sections = db.relationship("Section", secondary=class_section, backref="classes")

    def __init__(self, name):
        self.name = name


class ClassSchema(ma.ModelSchema):
    class Meta:
        model = Class
