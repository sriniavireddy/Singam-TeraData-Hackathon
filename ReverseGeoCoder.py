
from pygeocoder import Geocoder
import requests

def get_county_name(longitude, latitude, placeID = None):
    url_prefix = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
    #placeID and longitude and latitude
    key = 'AIzaSyAw-2MPkd3FbwnTjNpsaai1tsIzUk-B2aA'
    geocoder_obj = Geocoder(None, key)
    print "Lookup of Address Begin"
    results = geocoder_obj.reverse_geocode(longitude, latitude)
    print type(results)
    address = results.split()
    print address

#test the API
get_county_name(32.6044,-117.038)