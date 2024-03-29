# LowTemp

#### Video Demo:

#### Description:

Lowtemp is a weather application designed to save time when determining how to manage my horses in the evening.  Several factors need to be considered, specifically...

- The coldest nightly temperature
- How long it will be cold
- The precipitation chance, if any

These data are used to determine whether my horses need blankets, and/or whether they need to be brought into the barn to warm up.

#### Application Requirements

Initially, my only requirement was the ability to determine the low temperature in a given night.  In the southeast United States, horse blankets are typically required below 32 degrees.  Therefore, an output of the lowest temperature in a given evening seemed sufficient.

However, more data makes this decision easier.  For example, a temperature of 32 degrees may suggest that blankets are necessary for the evening.  But this temperature may only persist for a hour.  Not entirely necessary to use blankets in this scenario.

Conversely, a low temperature of 35 degrees may indicate that blankets are not necessary. But if rain is expected, it may be necessary to blanket the horses to protect them from heat loss while they are wet.

So the decision was made to include data on an hourly basis, visually represented as a crude bar graph.  The weather.gov API was selected as it provides hourly data for a given location, including temperature and precipitation chance.  This is almost always enough information to make a quick, informed decision about whether to blanket the horses on a given evening.

#### Application

The LowTemp application is implemented in python.  It is implemented as one file, lowtemp.py.

The program begins by implementing the following libraries:

- googlemaps, to geocode the input location
- os, to load the API key from the .env file
- re, to perform a regular expression to pull the date from the API data
- requests, to request the API data
- sys, to exit the program if the API is unavailable
- colorama, to colorize the bar graph
- dotenv, to load the API key from the .env file
- pprint, to help visualize the API json file

For security, the Googlemaps API key is located within a .env file.  This file is not uploaded to the github repository.

The main function of the program first calls the geocode function.  Geocode begins by asking the user for a location.  This location is sent to the googlemaps API to request the latitude and longitude of the user input.  The API key is also loaded from the .env file in this function.  The lat and long are retrieved from the API, rounded to four decimal places (per the weather.gov API docs), and then returned to the main function.  A short description of the address is also returned, in order to verify that the temperatures being graphed are indeed for the location the user wishes to see.

Returning to the main function, the first weather.gov request only serves to convert the latitude and longitude of my location (returned from googlemaps) into location data that the API can use.  A second API request is then made using this data, saving it as "forecast".  This forecast is returnded as a json.  These API requests are performed within a try-statement to handle any errors returned by the API.  If an error is encountered here, the program exits.

Here a for-loop begins which contains the f-string that will serve as the graph for every hour.  The enumerate function is used to count the number of loops.  This is used later to limit the number of hours that are shown in the graph.

The Forecast JSON objest is then broken down into the necessary parts that are needed for the graph using dictionary notation.  These are:

- temperature (degrees Fahrenheit)
- time (world time)
- precipitation (%)
- fc (a short forecast summary that is not currently used by the program)

A brief if-statement follows that blanks the precipitation chance if it is lower than 10%.  This eliminates some visual clutter in the graph.  Otherwise, the precipitation chance is saved as an f-string with a percentage sign and the unicode raindrop symbol.

Next, the pull_time function is called.  This uses a regular expression to save the time associated with each temperature.  It returns the hour as an integer.

Following that, the get_meridiem function is called.  This simply converts the 24-hour time into 12-hour time.

Now the f-string that is the graph is printed.  The f-string contains the notations for hours, temperature, and degrees.  It also calls two other functions, get_color and graph.

Get_color changes the color of the graph based on the temperature that is currently being graphed.  Temperatures are green by default.  Temperatures lower than 40 degrees show up as yellow, while temperatures lower than 32 show up as red.

Graph breaks down every temperature into a "bar graph".  This graph is made up of the unicode block character.  Each block represents two degrees.  When printed as a series of blocks, the blocks are seamless and appear as a long rectangle.  The graph!

This color and graph data is then returned to the f-string.  The color must be reset in several places to avoid coloring the whole printed line the same color.

Before the loop is performed again, an if-statement checks to see if the time is 12pm.  If so, and if 6 hours have been displayed, the loop exits.  This ensures that only one evening of temperatures are printed.  Otherwise the full week of hourly temperatures would be printed, which would be far too much information.

#### Next Steps

In the future, I'd like to implement a backup weather API in case weather.gov is down.

Also, I may implement the Forecast as its own class.  This wouldn't affect the usability of the program, but might allow easier modification in the future.


