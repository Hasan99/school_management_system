student_schema = {
    # person object
    "person_name": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                    "empty": False, "regex": "^[a-zA-Z]{2,20}([ .'a-zA-Z])*[a-zA-Z]+$"},
    "gender": {"type": "string", "minlength": 4, "maxlength": 10, "required": True, "nullable": False,
               "empty": False},
    "date_of_birth": {"type": "string", "required": True, "nullable": False, "empty": False},
    "b_form_cnic": {"type": "string", "minlength": 10, "maxlength": 50, "required": True, "nullable": False,
                    "empty": False, "regex": "^[a-zA-Z0-9-_]+$"},
    "branch_id": {"type": "integer", "min": 1, "required": True, "nullable": False},

    # class object
    "class_id": {"type": "integer", "min": 1, "required": True, "nullable": False},

    # section object
    "section_id": {"type": "integer", "min": 1, "required": True, "nullable": False}
}

parent_schema = {
    # address object
    "home_address": {"type": "string", "maxlength": 100, "required": True, "nullable": False, "empty": False},
    "city": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "province_state": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "country": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},

    # person object
    "person_name": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                    "empty": False, "regex": "^[a-zA-Z]{2,20}([ .'a-zA-Z])*[a-zA-Z]+$"},
    "b_form_cnic": {"type": "string", "minlength": 10, "maxlength": 50, "required": True, "nullable": False,
                    "empty": False, "regex": "^[a-zA-Z0-9-_]+$"},
    "phone_number": {"type": "string", "maxlength": 20, "required": True, "nullable": False, "empty": False,
                     "regex": r"^((\+92)|(0092))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{4}-\d{7}$"},
    "email": {"type": "string", "maxlength": 50, "empty": False,
              "regex": r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"},

    # "person_image": "Validated in Routes",
    # "address_id": "Inserted in Routes",

    "branch_id": {"type": "integer", "min": 1, "required": True, "nullable": False},

    # parent object
    "mother_name": {"type": "string", "minlength": 3, "maxlength": 100, "empty": False,
                    "regex": "^[a-zA-Z]{2,20}([ .'a-zA-Z])*[a-zA-Z]+$"},
    "occupation": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                   "empty": False},

    # "person_id": "Inserted in Routes"
}
