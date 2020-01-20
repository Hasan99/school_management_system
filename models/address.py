from main import db, ma


class Address(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    house_number = db.Column(db.String(50), nullable=False)
    block_sector = db.Column(db.String(50), nullable=False)
    town_area = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    province_state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    persons = db.relationship("Person", backref="address")

    def __init__(self, house_number, block_sector, town_area, city, province_state, country):
        self.house_number = house_number
        self.block_sector = block_sector
        self.town_area = town_area
        self.city = city
        self.province_state = province_state
        self.country = country


class AddressSchema(ma.ModelSchema):
    class Meta:
        model = Address
