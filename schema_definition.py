student_schema = {
    # address object
    "home_address": {"type": "string", "maxlength": 100, "required": True, "nullable": False, "empty": False},
    "city": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "province_state": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "country": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},

    # branch object
    "branch_id": {"type": "integer", "min": 1, "required": True, "nullable": False},

    # person object
    "person_name": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                    "empty": False, "regex": "^[a-zA-Z]{2,20}([ .'a-zA-Z])*[a-zA-Z]+$"},
    "gender": {"type": "string", "minlength": 4, "maxlength": 10, "required": True, "nullable": False,
               "empty": False},
    "date_of_birth": {"type": "string", "required": True, "nullable": False, "empty": False},
    "b_form_cnic": {"type": "string", "minlength": 10, "maxlength": 50, "required": True, "nullable": False,
                    "empty": False},

    # class object
    "class_id": {"type": "integer", "min": 1, "required": True, "nullable": False},

    # section object
    "section_id": {"type": "integer", "min": 1, "required": True, "nullable": False}
}

parent_schema = {
    "father_guardian": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                        "empty": False, "regex": "^[a-zA-Z]{2,20}([ .'a-zA-Z])*[a-zA-Z]+$"},
    "mother_name": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                    "empty": False, "regex": "^[a-zA-Z]{2,20}([ .'a-zA-Z])*[a-zA-Z]+$"},
    "occupation": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                   "empty": False},
    "income": {"type": "float", "min": 0, "required": True, "nullable": False},
    "phone_number": {"type": "string", "maxlength": 30, "required": True, "nullable": False, "empty": False},
}
