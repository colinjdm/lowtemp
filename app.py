# displays hourly temperatures from the current time until the next day at noon
# displays alert if temp is below 40 and/or below 32
# displays precipitation chance if over 10%

import googlemaps
import os
import re
import requests
import sys

from colorama import Fore
# dotenv for loading the .env file
from dotenv import load_dotenv
# flask
from flask import Flask, redirect, render_template, request
# graph.py defines bokeh graph
from graph import line_graph
# prettyprint for dict formatting
from pprint import pprint


app = Flask(__name__)


# load API key from .env
load_dotenv()


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        location = request.form.get('search')
        # initial request to determine location based on lat/long
        lat, lng, address = geocode(location)
        #print(f"Lat:      {lat}")
        #print(f"Long:    {lng}")
        #print(f"Location: {address}")
        # suppress errors when the API isn't responding
        try:
            # first request to obtain location URL
            r = requests.get(f'https://api.weather.gov/points/{lat},{lng}')
            # second request to obtain forecast
            forecast = requests.get(r.json()['properties']['forecastHourly'])
            periods = (forecast.json()['properties']['periods'])
        except Exception:
            sys.exit('API is not responding')


        # define empty lists where times, temps, and precip can be stored
        web_temps = []
        web_times = []
        web_precips = [] 

        for i, key in enumerate(periods):
            # enumerate will track the number of loops as 'i'
            temp = key['temperature']
            time = key['startTime']
            fc = key['shortForecast']
            precipitation = key['probabilityOfPrecipitation']['value']

            # append web lists with appropriate values every loop
            # make sure lists have same number of values
            web_temps.append(temp)
            web_precips.append(precipitation)

            if precipitation < 10:
                rain = ''
                fc = ''
            else:
                rain = f"\U0001F4A7 {precipitation}%"

            hour = pull_time(time)
            hour, meridiem = get_meridiem(hour)
            web_times.append(f'{hour} {meridiem}')

            # the variable {fc} can be added later to include a short forecast
            # print(f"{hour:2}:00 {meridiem} {get_color(temp) + graph(temp) + Fore.RESET}   {temp}\u00B0   {Fore.BLUE + rain + Fore.RESET}")
            # print(f"{key['detailedForecast']}")
            
            # stops displaying temps at noon as long as 6 hours have already been displayed
            if hour == 12 and meridiem == 'pm' and i > 6:
                break
        
        # test prints
        pprint(web_temps)
        pprint(web_times)
        pprint(web_precips)

        return render_template("weather.html", address=address, web_temps=web_temps, web_times=web_times, web_precips=web_precips)


def geocode(location):
    #location = input("Location: ")
    api_key = os.getenv('API_KEY')
    gmaps = googlemaps.Client(key=api_key)
    # geocode the address
    geocode_result = gmaps.geocode(location)
    # save address description
    address = geocode_result[0]['formatted_address']
    # save address lat and long
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    return round(lat, 4), round(lng, 4), address


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
    # adds blocks to a string for every 2 degrees of temperature
    string = ""
    # integer division
    temp = t // 2
    for _ in range(temp):
        string = string + "\u2588"
    return(string)


if __name__ == "__main__":
    main()