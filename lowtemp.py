# displays low temperature for the next 24 hours
# displays alert if temp is below 40 and/or below 32
import re
import requests

# prettyprint for dict formatting
from colorama import Fore
from pprint import pprint


def main():
    # initial request to determine location based on lat/long
    r = requests.get('https://api.weather.gov/points/32.6983,-85.6205')
    # second request to obtain forecast
    forecast = requests.get(r.json()['properties']['forecastHourly'])
    periods = (forecast.json()['properties']['periods'])
    #pprint(periods)

    for i, key in enumerate(periods):
        # enumerate will track the number of loops as 'i'
        temp = key['temperature']
        time = key['startTime']
        hour = pull_time(time)
        hour, meridiem = get_meridiem(hour)

        print(f"{hour:2}:00{meridiem} {get_color(temp) + snowflakes(temp)}  {temp}")
        #print(f"{key['detailedForecast']}")
        
        # stops displaying temps at noon as long as 6 hours have already been displayed
        if hour == 12 and meridiem == 'pm' and i > 6:
            break


def get_color(temp):
    if temp < 32:
        return Fore.RED
    elif temp < 40:
        return Fore.YELLOW
    else:
        return Fore.GREEN


def get_meridiem(hour):
    # allows converting from world time to meridiem
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


def snowflakes(t):
    # a crude graph
    # adds snowflakes (asterisks) to a string for every 10 degrees of temperature
    string = ""
    # integer division
    temp = t // 2
    for _ in range(temp):
        string = string + "\u2588"
    return(string)


if __name__ == "__main__":
    main()