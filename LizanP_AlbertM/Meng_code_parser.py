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

      
