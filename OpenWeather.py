'''
Reference URL: https://openweathermap.org/current
'''

import requests
import json
from OpenWeatherException import OpenWeatherException as OWException


class OpenWeather:
    def __init__(self):
        print("Instantiate OpenWeather Object")
        self.API_KEY = "349573272b4f8cf9a6c3ce64750b5d83"
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        self.TEMP_UNIT = 'imperial'

    def url_constructor(self, city_name=None, city_zip_code=None):
        print("[RS] Constructing OpenWeather API URL")
        if city_name is not None and city_zip_code is None:
            complete_url = self.BASE_URL + "q=" + str(
                city_name) + "&APPID=" + self.API_KEY + "&mode=json&units=" + self.TEMP_UNIT
        elif city_name is None and city_zip_code is not None and isinstance(city_zip_code, int):
            complete_url = self.BASE_URL + "zip=" + str(
                city_zip_code) + "&APPID=" + self.API_KEY + "&units=" + self.TEMP_UNIT
        else:
            raise OWException("Missing city information")
        return complete_url

    def make_weather_api_request(self, target_url):
        print("[RS] Making OpenWeather API request")
        if target_url is not None:
            try:
                response = requests.get(target_url)
                json_response = response.json()
            except:
                raise OWException("Could not make the weather update API request")
            return json_response

    def get_current_temperature(self, json_response):
        print("[RS] Getting current temperature from the JSON response")
        if json_response is not None and json_response["cod"] != "404":
            # Reading "main" content
            MAIN_CONTENT = json_response["main"]
            current_temperature = MAIN_CONTENT["temp"]
        else:
            raise OWException("No City/Temperature reading found")
        return current_temperature

    def get_current_weather_report(self, json_response):
        print("[RS] Getting weather report from the JSON response")
        if json_response is not None and json_response["cod"] == "200":
            # Reading "main" content
            MAIN_CONTENT = json_response["main"]
            current_temperature = MAIN_CONTENT["temp"]
            current_pressure = MAIN_CONTENT["pressure"]
            current_humidiy = MAIN_CONTENT["humidity"]

            # Reading "weather" content
            WEATHER_CONTENT = json_response["weather"]
            weather_description = WEATHER_CONTENT[0]["description"]

            print(" Temperature (F) = " + str(current_temperature) +
                  "\n atmospheric pressure (hPa) = " + str(current_pressure) +
                  "\n humidity (%) = " + str(current_humidiy) +
                  "\n description = " + str(weather_description))
        else:
            raise OWException("No weather report / City found")




########################################TEST CODE#############################################################
# if __name__ == '__main__':
#     myWeather = OpenWeather()
    # city = 94040
    # URL = myWeather.url_constructor(None, city)
    # print(URL)
#     weatherJson = myWeather.get_weather(URL)
#     # weatherReport = myWeather.get_weather_report(weatherJson)
#     temperature = myWeather.get_current_temperature(weatherJson)
#     print(temperature)
