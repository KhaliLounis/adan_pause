import geocoder
import requests


#get ip adress function
def get_ip_address():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    ip_address = ip_data['ip']
    return ip_address
ip_address = get_ip_address()

#get location cordination

def get_cords():
    g = geocoder.ip(ip_address)
    latlng= g.latlng
latlng =  get_cords

print(latlng)




