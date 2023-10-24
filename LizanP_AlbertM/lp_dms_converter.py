def dms2dd(coordinates):
    coordinates = coordinates.upper()
    if int(coordinates.split()[0]) in range(0, 181) and int(coordinates.split()[1]) in range(0, 60) and int(coordinates.split()[2]) in range(0, 60) and int(coordinates.split()[4]) in range(0, 91) and int(coordinates.split()[5]) in range(0, 60) and int(coordinates.split()[6]) in range(0, 60):
        longitude_dd = int(coordinates.split()[0]) + int(coordinates.split()[1])/60 + int(coordinates.split()[2])/3600
        latitude_dd = int(coordinates.split()[4]) + int(coordinates.split()[5])/60 + int(coordinates.split()[6])/3600
        if "W" in coordinates:
            longitude_dd *= -1
        if "S" in coordinates:
            latitude_dd *= -1
        return f'({longitude_dd:.5f},{latitude_dd:.5f})'
    else:
        return (None, None)