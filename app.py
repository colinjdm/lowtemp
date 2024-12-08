# displays hourly temperatures from the current time until the next day at noon
# displays alert if temp is below 40 and/or below 32
# displays precipitation chance if over 10%

import googlemaps
import os
import re

from colorama import Fore
# dotenv for loading the .env file
from dotenv import load_dotenv
# flask
from flask import Flask, redirect, render_template, request
from openweathermap import get_weather
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
        # get search term from html
        location = request.form.get('search')
        # initial request to determine location based on lat/long
        lat, lng, address = geocode(location)
        web_times, web_temps, web_precips = get_weather(lat, lng)
        #pprint(times)
        #pprint(web_temps)

        # hour = pull_time(time)
        # web_times = []
        # for i in range(len(times)):
        #    time = get_meridiem(times[i])
        #    web_times.append(time)
        # print(web_times)

        # web_times.append(f'{hour} {meridiem}')
        
        # stops displaying temps at noon as long as 6 hours have already been displayed
        # if hour == 12 and meridiem == 'pm' and i > 6:
        #    break

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
    time = (f'{hour} {meridiem}')
    return (time)


def pull_time(s):
    # pulls time out of the api string using regex
    hour = re.search(r"T([0-9][0-9]):", s)
    # convert the string into an integer
    hour = hour[0].replace(":", "")
    hour = hour.replace("T", "")
    return int(hour)


if __name__ == "__main__":
    main()