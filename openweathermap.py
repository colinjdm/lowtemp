import datetime
import json
import os
import requests
import sys

# dotenv for loading the .env file
from dotenv import load_dotenv
from pprint import pprint


# load API key from .env
load_dotenv()

def get_weather(lat, lon):

    api_key = os.getenv('API_key')
    try:
        r = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=imperial')
        weather = r.json()
        hourly_weather = r.json()['hourly']
    except Exception:
        sys.exit('API is not responding')

    # moon phase
    moon_phase = weather['daily'][0]['moon_phase']
    #print(f'Moon phase: {moon_phase}')

    hourly_temp = []
    hourly_time = []
    hourly_precip = []

    for i, key in enumerate(hourly_weather):

        # hourly precipitation chance
        precip = weather['hourly'][i]['pop'] * 100
        #print(weather['hourly'][i])
        hourly_precip.append(precip)

        # unix time conversion
        time = (datetime.datetime.fromtimestamp(key['dt']))
        # pull whatever info is needed from the datetime string
        # currently --> day, month date, time (24hr)
        time = datetime.datetime.strftime(time, '%A, %B %d, %H:00')
        hourly_time.append(time)

        # hourly temperature
        hourly_temp.append(round(key['temp']))
    print(f'{len(hourly_time)},{len(hourly_temp)},{len(hourly_precip)}')
    return(hourly_time, hourly_temp, hourly_precip)


if __name__ == "__main__":
    get_weather()
