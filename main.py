import geocoder
import requests


def get_ip_address():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    ip_address = ip_data['ip']
    return ip_address
ip_address = get_ip_address()

def get_latitude_longitude(ip_address):
    g = geocoder.ip(ip_address)
    if g.ok:
        latitude, longitude = g.latlng
        return latitude, longitude
    else:
        return None
print(get_latitude_longitude(ip_address))
