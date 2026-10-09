WEATHER INFORMATION SYSTEM

  The Weather Information System is a Python-based application designed to provide users with the current weather 
information of any city they enter. The application uses the Open-Meteo Geocoding API to identify the geographical
coordinates, namely latitude and longitude, of the requested city and then uses these coordinates to obtain the current 
weather data from the Open-Meteo Weather API. The Python `requests` module is used to communicate with these external APIs,
while the JSON responses received from the APIs are processed using Python dictionaries and lists to extract the required 
information. The application includes a simple interactive interface that allows users to enter different cities and retrieve
their weather information repeatedly during a single execution. It also incorporates basic error handling to deal with
invalid or unrecognized city names and unsuccessful API requests, preventing the program from terminating unexpectedly. 
Through this project, concepts such as API communication, HTTP requests, JSON data processing, dictionary and 
list operations, user input, loops, conditional statements, exception handling, and dynamic URL construction are practically 
implemented in Python.

  The Weather Information System also provides location-specific information by displaying the country associated with the entered city. It retrieves current temperature, weather conditions, wind speed, and relative humidity using data from the Open-Meteo API. The application includes basic error handling to manage unsuccessful weather requests and checks whether a city exists before attempting to retrieve its weather information. Users can search for multiple cities in a single session without restarting the program. This project strengthened my understanding of working with external APIs, handling JSON responses, extracting information from dictionaries and lists, using conditional statements to interpret weather codes, and implementing loops and exception handling to create a more reliable Python application.

