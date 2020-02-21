from app import db, ma
from datetime import datetime


# parent table
class Address(db.Model):
    __tablename__ = "address"
    address_id = db.Column(db.Integer, primary_key=True)
    home_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    province_state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    # person = db.relationship("Person", backref="address")
    # branch = db.relationship("Branch", backref="address")

    def __init__(self, home_address, city, province_state, country):
        self.home_address = home_address
        self.city = city
        self.province_state = province_state
        self.country = country


class AddressSchema(ma.ModelSchema):
    class Meta:
        model = Address


# parent table
class Branch(db.Model):
    __tablename__ = "branch"
    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(200), nullable=False)

    # address = db.relationship("Address", backref="branch", uselist=False)
    # person = db.relationship("Person", backref="branch")

    def __init__(self, branch_name):
        self.branch_name = branch_name


class BranchSchema(ma.ModelSchema):
    class Meta:
        model = Branch


# parent table
class Parent(db.Model):
    __tablename__ = "parent"
    parent_id = db.Column(db.Integer, primary_key=True)
    father_guardian = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    income = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)

    # student = db.relationship("Student", backref="parent")

    def __init__(self, father_guardian, mother_name, occupation, income, phone_number):
        self.father_guardian = father_guardian
        self.mother_name = mother_name
        self.occupation = occupation
        self.income = income
        self.phone_number = phone_number


class ParentSchema(ma.ModelSchema):
    class Meta:
        model = Parent


# parent table
class Role(db.Model):
    __tablename__ = "role"
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # user = db.relationship("User", backref="role")

    def __init__(self, name):
        self.name = name


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role


# child table
class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    b_form_cnic = db.Column(db.String(50), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)
    address_id = db.Column(db.Integer, db.ForeignKey("address.address_id"), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"), nullable=False)
    address = db.relationship("Address", backref="person")
    branch = db.relationship("Branch", backref="person")

    # address = db.relationship("Address", back_populates="person")
    # branch = db.relationship("branch", back_populates="person")
    # contact = db.relationship("contact", back_populates="person")


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person


# child table
class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), nullable=False, unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.branch_id"), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("parent.parent_id"), nullable=False)
    person = db.relationship("Person", backref="student")
    branch = db.relationship("Branch", backref="student")
    parent = db.relationship("Parent", backref="student")

    # parent = db.relationship("parent", back_populates="student")
    # person = db.relationship("person", back_populates="student")
    # branch = db.relationship("branch", back_populates="student")


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student


# child table
class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"), nullable=False)
    role = db.relationship("Role", backref="user")

    # role = db.relationship("role", back_populates="user")


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


# child table
class Contact(db.Model):
    __tablename__ = "contact"
    contact_id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), default="not available")
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    person = db.relationship("Person", backref="contact")

    # person = db.relationship("person", back_populates="contact")


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = Contact


# parent table
class Section(db.Model):
    __tablename__ = "section"
    section_id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(100), nullable=False, unique=True)

    # Class = db.relationship("Class", backref="section")

    def __init__(self, section_name):
        self.section_name = section_name


class SectionSchema(ma.ModelSchema):
    class Meta:
        model = Section


# child table
class_section = db.Table("class_section",
                         db.Column("class_id", db.Integer, db.ForeignKey("class.class_id"), nullable=False),
                         db.Column("section_id", db.Integer, db.ForeignKey("section.section_id"), nullable=False),
                         db.Column("student_id", db.Integer, db.ForeignKey("student.student_id"), nullable=False),
                         db.Column("year_of_passing", db.String(30), default="not available")
                         )


# parent table
class Class(db.Model):
    __tablename__ = "class"
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    section = db.relationship("Section", secondary="class_section", backref="class")

    def __init__(self, class_name):
        self.class_name = class_name


class ClassSchema(ma.ModelSchema):
    class Meta:
        model = Class
