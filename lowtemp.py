# displays low temperature for the next 24 hours
import json
import requests
import sys

# prettyprint for dict formatting
from pprint import pprint


def main():
    r = requests.get('https://api.weather.gov/points/32.6983,-85.6205')
    #pprint(r.json())

    forecast = requests.get(r.json()['properties']['forecastHourly'])

    periods = (forecast.json()['properties']['periods'])

    #pprint(periods)

    for key in periods:
        temp = key['temperature']
        time = key['endTime']
        snowflakes = coldness(temp)
        print(f"At {time} the temperature will be {temp} {snowflakes}")


def coldness(t):
    string = f""
    snowflakes = t // 10
    for i in range(snowflakes):
        string = string + "*"

    return(string)


if __name__ == "__main__":
    main()