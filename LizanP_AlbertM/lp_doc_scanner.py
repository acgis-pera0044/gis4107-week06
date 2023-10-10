def has_x_code(in_text):
    for t in in_text:
        possible_string = in_text[start_sequence:end_sequence]

        if possible_string == "Tx6op3":
            return True
            break
        elif end_sequence == len(in_text):
            return False
        start_sequence += 1
        end_sequence += 1
