def get_coords_from_gpx(gpx):
    gpx_list = gpx.split()
    if "trkpt" in gpx_list[0]:
        lat_value = gpx_list[1].split('"')[1]
        long_value = gpx_list[2].split('"')[1]
        return f'({long_value},{lat_value})'
    else:
        return None, None
