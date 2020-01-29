student_schema = {
    # address object
    "house_number": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "block_sector": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "town_area": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "city": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "province_state": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},
    "country": {"type": "string", "maxlength": 50, "required": True, "nullable": False, "empty": False},

    # branch object
    "branch_name": {"type": "string", "maxlength": 200, "required": True, "nullable": False, "empty": False},

    # person object
    "person_name": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                    "empty": False},
    "father_name": {"type": "string", "minlength": 3, "maxlength": 100, "required": True, "nullable": False,
                    "empty": False},
    "gender": {"type": "string", "minlength": 4, "maxlength": 10, "required": True, "nullable": False,
               "empty": False},
    "date_of_birth": {"type": "string", "minlength": 10, "maxlength": 10, "required": True, "nullable": False,
                      "empty": False},
    "b_form_cnic": {"type": "string", "minlength": 10, "maxlength": 50, "required": True, "nullable": False,
                    "empty": False},
}
