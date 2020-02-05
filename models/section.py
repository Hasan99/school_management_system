if __name__ == '__main__':
    from main import db, ma


# parent table
class Section(db.Model):
    section_id = db.Column(db.Ineteger, primary_key=True)
    section_name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, section_name):
        self.section_name = section_name


class SectionSchema(ma.ModelSchema):
    class Meta:
        model = Section
