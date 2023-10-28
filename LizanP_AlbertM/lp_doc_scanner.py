def has_x_code_first_try(in_text):
    start_sequence = 0
    end_sequence = 6
    for t in in_text:
        possible_string = in_text[start_sequence:end_sequence]
        if possible_string == "Tx6op3":
            return True
        elif end_sequence == len(in_text):
            return False
        start_sequence += 1
        end_sequence += 1

def has_x_code(in_text):
    """The function evaluates if the string "Tx6op3" is found in the argument

    Args:
        in_text (string): any length

    Returns:
        True or False: This function will return True if the exact encoded string is found in in_text and False if it is not found
    """
    if "Tx6op3" in in_text:
        return True
    else:
        return False

def get_x_code_position(in_text):
    """This function returns the position in the string where the encoded string begins

    Args:
        in_text (string): any length

    Returns:
        int: This function will associate 1 with the first character in in_text. If the code is not found, this function will return -1
    """
    position = in_text.find("Tx6op3")
    if position != -1:
        return position + 1
    else:
        return position
