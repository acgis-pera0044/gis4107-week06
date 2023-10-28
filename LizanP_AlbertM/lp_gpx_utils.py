def get_coords_from_gpx(gpx):
    """This function take a string with the format of a GPX file and returns both longitude and latitude values

    Args:
        gpx (string): string with the format of a GPX file <trkpt lat="45.38895" lon="-75.7472631">

    Returns:
        floats: returns two floats representing decimal degree longitude and latitude
    """
    gpx_list = gpx.split()
    if "trkpt" in gpx_list[0]:
        lat_value = float(gpx_list[1].split('"')[1])
        long_value = float(gpx_list[2].split('"')[1])
        return long_value, lat_value
    else:
        return None, None

def get_coords_from_gpx_first_try(gpx):
    if "trkpt" in gpx:
        index_lat = gpx.find("lat=")
        index_lon = gpx.find("lon=")
        lat_value = gpx[index_lat+5 : index_lon-2]
        long_value = gpx[index_lon+5 : len(gpx)-2]
        return f'({long_value},{lat_value})'
    else:
        return None, None