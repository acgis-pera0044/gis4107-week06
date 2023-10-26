def is_valid_phone_number(phone_number):
    """
    To judge whether a string is a standard phone number format

    Args:
        phone_number (string): string to be judged 

    Returns:
        Boolean: True when the string is a standard phone number, False when it is not.
    """
    result=True

    length=len(phone_number)

    if length != 12:
     result=False

    if phone_number[3]and phone_number[7] != '-':
     result=False
    #Judge whether the number has the dash at the right position

    for i in range(length):

        if i==3 or i==7: continue
        elif phone_number[i].isdigit():  
             continue
            #Judge the letter should be a number
    
        else: result=False
        break
            #If there is non-digit exist, the result will be False and terminate
    
    return result

