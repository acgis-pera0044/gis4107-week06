def dms2dd(dms):
   """
      to judge whether the input string is the correct format of a coordination
      and to transfer the DMS format to DD format

   Args:
       dms (string): the DMS format of a coordination

   Returns:
       DD format of a coordination when the DMS is a legal data.
   """
   lon_lat=dms.split()
   if len(lon_lat)!=8:
      return None,None
   if float(lon_lat[0])<0 or float(lon_lat[0])>180:
      return None,None
   if float(lon_lat[1])<0 or float(lon_lat[1])>59:
       return None,None
   if float(lon_lat[2])<0 or float(lon_lat[2])>59:
       return None,None
   if float(lon_lat[4])<0 or float(lon_lat[4])>90:
       return None,None
   if float(lon_lat[5])<0 or float(lon_lat[5])>59:
       return None,None
   if float(lon_lat[6])<0 or float(lon_lat[6])>59:
       return None,None
    
   lon_dd = float(lon_lat[0]) + float(lon_lat[1]) / 60 + float(lon_lat[2]) / 3600
   if lon_lat[3]=='W' or lon_lat[3]=='w' :
       lon_dd=-lon_dd

   lat_dd = float(lon_lat[4]) + float(lon_lat[5]) / 60 + float(lon_lat[6]) / 3600
   if lon_lat[7]=='S' or lon_lat[7]=='s':
       lat_dd=-lat_dd

   return lon_dd,lat_dd