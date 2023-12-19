# displays hourly temperatures from the current time until the next day at noon
# displays alert if temp is below 40 and/or below 32
# displays precipitation chance if over 10%

import re
import requests

from colorama import Fore
# prettyprint for dict formatting
from pprint import pprint


def main():
    # initial request to determine location based on lat/long
    r = requests.get('https://api.weather.gov/points/32.6983,-85.6205')
    # second request to obtain forecast
    forecast = requests.get(r.json()['properties']['forecastHourly'])
    periods = (forecast.json()['properties']['periods'])
    # pprint(periods)

    for i, key in enumerate(periods):
        # enumerate will track the number of loops as 'i'
        temp = key['temperature']
        time = key['startTime']
        fc = key['shortForecast']
        precipitation = key['probabilityOfPrecipitation']['value']
        #print(precipitation)
        
        if precipitation < 10:
            rain = ''
            fc = ''
        else:
            rain = f"\U0001F4A7 {precipitation}%"

        hour = pull_time(time)
        hour, meridiem = get_meridiem(hour)

        # the variable {fc} can be added later to include a short forecast
        print(f"{hour:2}:00 {meridiem} {get_color(temp) + graph(temp) + Fore.RESET}  {temp}    {Fore.BLUE + rain + Fore.RESET}")
        #print(f"{key['detailedForecast']}")
        
        # stops displaying temps at noon as long as 6 hours have already been displayed
        if hour == 12 and meridiem == 'pm' and i > 6:
            break


def get_color(temp):
    if temp <= 32:
        return Fore.RED
    elif temp <= 40:
        return Fore.YELLOW
    else:
        return Fore.GREEN


def get_meridiem(hour):
    # allows converting from 24-hour time to 12-hour time
    if hour == 0:
        meridiem = 'am'
        hour = 12
    elif hour < 12:
        meridiem = 'am'
    elif hour == 12:
        meridiem = 'pm'
    else:
        meridiem = 'pm'
        hour = hour - 12
    return (hour, meridiem)


def pull_time(s):
    # pulls time out of the api string using regex
    hour = re.search(r"T([0-9][0-9]):", s)
    # convert the string into an integer
    hour = hour[0].replace(":", "")
    hour = hour.replace("T", "")
    return int(hour)


def graph(t):
    # a crude graph
    # adds blocks to a string for every 10 degrees of temperature
    string = ""
    # integer division
    temp = t // 2
    for _ in range(temp):
        string = string + "\u2588"
    return(string)


if __name__ == "__main__":
    main()