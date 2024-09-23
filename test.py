from geolocation.geolocation import GeoLocation

geo = GeoLocation(proxy="http://user:pass@ip:port")

# Call the get_geolocation method
geolocation_data = geo.get_geolocation()

# Print the geolocation data
print(geolocation_data)