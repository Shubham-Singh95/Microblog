import requests


def req_weather_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=1ae2db6ba6be6ae46eeadb' \
          '67380c890b&units=metric'.format(city)
    return requests.get(url)
