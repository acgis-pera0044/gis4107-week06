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
    if "Tx6op3" in in_text:
        return True
    else:
        return False

def get_x_code_position(in_text):
    position = in_text.find("Tx6op3")
    if position != -1:
        return position + 1
    else:
        return position
