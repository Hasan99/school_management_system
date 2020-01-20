from main import db, ma


class Section(db.Model):
    section_id = db.Column(db.Ineteger, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


class SectionSchema(ma.ModelSchema):
    class Meta:
        model = Section
