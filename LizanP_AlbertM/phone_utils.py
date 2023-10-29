def is_valid_phone_number(phone_number):
    """This function evaluates if the phone number has the form NNN-NNN-NNNN

    Args:
        phone_number (string): the phone number that we want to evaluate

    Returns:
        True or False: It returns True if the phone number has all numbers and has the format NNN-NNN-NNNN. It returns false if any character is not a number (except the dashes) or it does not have the above format
    """
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