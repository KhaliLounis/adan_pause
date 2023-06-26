import requests
import datetime

def get_prayer_times(latitude, longitude):
    
    todays_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # get the adan times for today
    response= requests.get(f"https://api.aladhan.com/v1/timings/{todays_date}?latitude={latitude}&longitude={longitude}&method=2")

    data= response.json()['data']['timings']
    keys_to_remove = ['Sunrise', 'Sunset', 'Midnight', 'Imsak', 'Firstthird', 'Lastthird']

    #get only prayers in the dictionary
    for key in keys_to_remove:
        data.pop(key, None)
        
    return data.values()
