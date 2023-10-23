def get_db_link(building_code):
    link_letter = building_code[4:6]
    link_number = building_code[10:13]
    db_link = link_letter + "-" + link_number
    return db_link