def dms2dd(coordinates):
    """The code takes a string that contains the values of long and lat with the format DDD MM SS W|E DD MM SS N|S, and returns two floats representing decimal degress longitude and latitude

    Args:
        coordinates (string): DDD MM SS W|E DD MM SS N|S

    Returns:
        floats: values of latitude and longitude in decimal degrees with 5 decimals
    """
    coordinates = coordinates.upper()
    if int(coordinates.split()[0]) in range(0, 181) and int(coordinates.split()[1]) in range(0, 60) and int(coordinates.split()[2]) in range(0, 60) and int(coordinates.split()[4]) in range(0, 91) and int(coordinates.split()[5]) in range(0, 60) and int(coordinates.split()[6]) in range(0, 60):
        longitude_dd = round(int(coordinates.split()[0]) + int(coordinates.split()[1])/60 + int(coordinates.split()[2])/3600, 5)
        latitude_dd = round(int(coordinates.split()[4]) + int(coordinates.split()[5])/60 + int(coordinates.split()[6])/3600, 5)
        if "W" in coordinates:
            longitude_dd *= -1
        if "S" in coordinates:
            latitude_dd *= -1
        return longitude_dd, latitude_dd
    else:
        return None, None