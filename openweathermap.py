import datetime
import requests

from pprint import pprint

API_key = 'e1adbe8a851f3f58b8d9dcd898aafacd'
lat = 32.73515023952092
lon = -85.57369718339207

def get_weather(lat, lon):
    r = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}')
    hourly_weather = r.json()['hourly']

    hourly_temp = []
    hourly_time = []
    for i, key in enumerate(hourly_weather):
        #print(key['dt'])

        # unix time conversion
        time = (datetime.datetime.fromtimestamp(key['dt']))
        
        # pull just the hour from the datetime string
        # might move this into app.py so I can keep this info moving forward
        # time = datetime.datetime.strftime(time, '%H')

        hourly_time.append(time)

        # kelvin to fahrenheit conversion
        hourly_temp.append(round(((key['temp'] - 273.15) * (9 / 5)) + 32))

        # print debug
    for i in range(len(hourly_temp)):
        print(f'{hourly_time[i]}, {hourly_temp[i]} degrees')


if __name__ == "__main__":
    get_weather()
