from app import db, ma


# parent table
class Address(db.Model):
    __tablename__ = "address"
    address_id = db.Column(db.Integer, primary_key=True)
    home_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    province_state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    # person = db.relationship("Person", back_populates="address")
    # branch = db.relationship("Branch", back_populates="address")

    def __init__(self, home_address, city, province_state, country):
        self.home_address = home_address
        self.city = city
        self.province_state = province_state
        self.country = country


class AddressSchema(ma.ModelSchema):
    class Meta:
        model = Address
