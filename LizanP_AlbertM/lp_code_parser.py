def get_db_link(building_code):
    """The function takes the bulding code in the form NN-LLL-NNNNNN-NNN and return the link that can be used between 2 database tables

    Args:
        building_code (string): the building code must have the format NN-LLL-NNNNNN-NNN

    Returns:
        string: The link is the last 2 letters of the LLL part and the last 3 numbers of the second numbered part
    """
    link_letter = building_code[4:6]
    link_number = building_code[10:13]
    db_link = link_letter + "-" + link_number
    return db_link