def get_coords_from_gpx(gpx): 
   """
   to judge whether the input string is a legal coordination data
   If the data is legal, then return the longitude and latitude data 
   If the data is illegal, then return None
   
   Args:
       the input string

   Returns:
       the coordinate data or None
   """
    
   data_lat=''
   data_lon=''

   if gpx.find('trkpt')!=-1:

        lat_start= gpx.find('lat="')+5  # Passing five letter positions of 'lat="' to number position
        for i in range(lat_start,len(gpx),1):
          if gpx[i]=='"' :
             break   
          else:data_lat+=gpx[i]



        lon_start=gpx.find('lon="')+5 # Passing five letter positions of 'lon="' to number position
        for i in range(lon_start,len(gpx),1):
          if gpx[i]=='"' :
             break
          else:data_lon+=gpx[i]


   else: return None,None 

   return  data_lon,data_lat
    


