# displays low temperature for the next 24 hours
import requests

# prettyprint for dict formatting
from pprint import pprint


def main():
    r = requests.get('https://api.weather.gov/points/32.6983,-85.6205')
    #pprint(r.json())
    forecast = requests.get(r.json()['properties']['forecastHourly'])
    periods = (forecast.json()['properties']['periods'])
    #pprint(periods)

    for i, key in enumerate(periods):
        # enumerate tracks the number of loops as 'i'
        temp = key['temperature']
        time = key['endTime']
        print(f"At {time} the temperature will be {temp} {snowflakes(temp)}")
        
        # number of hours to stop at
        # default api shows about 5 days
        limit = 24
        if i == limit:
            break


def snowflakes(t):
    # adds snowflakes (asterisks) to a string for every 10 degrees of temperature
    # initialize empty string
    string = ""
    # integer division
    temp = t // 10
    for _ in range(temp):
        string = string + "*"
    return(string)


if __name__ == "__main__":
    main()