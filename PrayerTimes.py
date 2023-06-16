import requests
import datetime

def get_prayer_times():
    
    todays_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # get the adan times for today
    response= requests.get(f"https://api.aladhan.com/v1/timings/{todays_date}?latitude=35.88635738460494&longitude=3.772759469317077&method=2")

    k=response.json()['data']['timings']
    keys_to_remove = ['Sunrise', 'Sunset', 'Midnight', 'Imsak', 'Firstthird', 'Lastthird']

    #get only prayers in the dictionary
    for key in keys_to_remove:
        k.pop(key, None)
        
    return k.values()