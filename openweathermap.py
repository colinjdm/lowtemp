import datetime
import requests
import sys

from pprint import pprint

API_key = 'e1adbe8a851f3f58b8d9dcd898aafacd'

def get_weather(lat, lon):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}&units=imperial')
        hourly_weather = r.json()['hourly']
    except Exception:
        sys.exit('API is not responding')

    hourly_temp = []
    hourly_time = []
    for i, key in enumerate(hourly_weather):
        #pprint(key['dt'])

        # unix time conversion
        time = (datetime.datetime.fromtimestamp(key['dt']))
        
        # pull whatever info is needed from the datetime string
        # currently --> year, month date, time (24hr)
        time = datetime.datetime.strftime(time, '%Y, %B %d, %H:00')

        hourly_time.append(time)
        hourly_temp.append(round(key['temp']))

    return(hourly_time, hourly_temp)


if __name__ == "__main__":
    get_weather()
