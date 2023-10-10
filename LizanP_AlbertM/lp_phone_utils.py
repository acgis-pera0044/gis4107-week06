def is_valid_phone_number(phone_number):
    if len(phone_number) == 12:
        if phone_number[0:3].isdigit() and phone_number[4:7].isdigit() and phone_number[8:12].isdigit():
            if phone_number.index("-") == 3 and phone_number.rindex("-") == 7:
                return True
            else:
                return False
        else:
            return False
    else:
        return False