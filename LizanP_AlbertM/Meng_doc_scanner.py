
def has_x_code(in_text):
   """
    to judge whether a defined string is contained in the given string 

   Args:
       the given string

   Returns:
       True or False for the judging result
   """

   string = in_text
   national_code = "Tx6op3"

   if string.find(national_code) != -1:
    return True
   else:
    return False


def get_x_code_position(in_text):
   """
   to return the position of a defined string within a given string

   Args:
       the given string

   Returns:
       the position of the first letter of the defined string
   """
  
   string = in_text
   national_code = "Tx6op3"

   position = string.find(national_code)
   return position+1

