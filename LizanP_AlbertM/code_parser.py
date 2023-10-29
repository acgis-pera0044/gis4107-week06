def get_db_link(building_code):
  """to create a link between two database tables 
     the last two letters of the LLL part and the last three numbers of the second numbered part need to be extracted and pasted together

  Args:
      building_code (string): the original string

  Returns:
      string after required linking.
  """
    
  link="" 

  for i in range(len(building_code)) :
    if i==4:
      link+=building_code[i]
      continue

    if i==5:
      link+=building_code[i]
      link+="-"
      continue

    if i==10:
      link+=building_code[i]
      continue

    if i==11:
      link+=building_code[i]
      continue

    if i==12:
      link+=building_code[i]
      continue

  return link

def get_db_link_lizan(building_code):
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
