from app import db, ma


# parent table
class Section(db.Model):
    __tablename__ = "section"
    section_id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, section_name):
        self.section_name = section_name


class SectionSchema(ma.ModelSchema):
    class Meta:
        model = Section
