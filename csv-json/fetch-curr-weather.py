"""
Project: Fetching Current Weather Data

This project is meant to get the current weather and that of the next 2 days using the OpenWeather API,
the program does the following:
• Reads the requested location from the command line.
• Downloads JSON weather data from OpenWeatherMap.org.
• Converts the string of JSON data to a Python data structure.
• Prints the weather for today and the next two days.

Going to use OpenWeather's 5 day / 3-hour API that includes weather forecast data with 3-hour step.
"""

# import relevant modules
import requests, json, sys

# OpenWeather API Key
openwthr_key = input()

# get location from the command line
if len(sys.argv) < 2:
    print("Usage: fetch-curr-weather.py search_location.")
    sys.exit()

search_location = '%20'.join(sys.argv[1:])

forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={search_location}&appid={openwthr_key}"

try:
    # downloading the weather data from the API url
    res_obj = requests.get(forecast_url)
    res_obj.raise_for_status()
    pass
except Exception as req_exc:
    print(req_exc)

else:
    # print(res_obj.status_code)
    # getting the response in JSON format
    weather_data = res_obj.json()["list"]

    # weather description for day today
    today_weather = weather_data[0]["weather"][0]["description"]

    # weather description for tomorrow
    tomorrow_weather = weather_data[4]["weather"][0]["description"]

    # weather description for day after tomorrow
    next_weather = weather_data[12]["weather"][0]["description"]

    print(f"Current weather in {search_location.capitalize()}:\n{today_weather}\n")

    print(f"Tomorrow:\n{tomorrow_weather}\n")

    print(f"Day after tomorrow:\n{next_weather}")
    # print(len(weather_data))
