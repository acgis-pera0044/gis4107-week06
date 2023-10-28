def get_coords_from_gpx(gpx):
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