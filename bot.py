#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response, request
from datetime import datetime
import configparser
import json
import urllib

app = Flask(__name__)

def url_builder(city):
    user_api = 'eb2bd9c36757e7f1953cabf1994e84ac'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/forecast/daily?q='
    full_api_url = api + str(city) + '&mode=json&units=' + unit + '&APPID=' + user_api + '&cnt=7'
    return full_api_url

@app.route('/', methods=['POST'])
def get_weather():
    data = request.form
    city = data["text"]
    full_api_url = url_builder(city)
    req = urllib.urlopen(full_api_url)
    output = req.read().decode('utf-8')
    test = json.loads(output)
    payload_text = build_response_text(test)
    return payload_text

def get_embedded_icon_url(icon_code, desc):
    return '![desc](http://openweathermap.org/img/w/{code}.png "{desc}")'.format(code=icon_code, desc=desc)

def get_day_weather_line(day):
    day_weekday = datetime.fromtimestamp(day['dt']).strftime("%A")
    day_month = datetime.fromtimestamp(day['dt']).strftime("%b")
    day_day = datetime.fromtimestamp(day['dt']).strftime("%d")
    day_info_date = """{weekday}, {month}. {day_number}""".ljust(25).format(weekday=day_weekday, month=day_month, day_number=day_day)
    day_desc = day['weather'][0]['description']
    day_desc.ljust(50)
    day_temp_high = int(day['temp']['max'])
    day_temp_low = int(day['temp']['min'])
    day_humidity = day['humidity']
    day_icon = get_embedded_icon_url(day['weather'][0]['icon'], day_desc)
    return "| {day_info_date_param} | {desc_param}  {day_icon_param} | {day_temp_high_param} °C | {day_temp_low_param} °C  | {day_humidity_param} |\n".format(day_info_date_param=day_info_date, desc_param=day_desc, day_icon_param=day_icon, day_temp_high_param=day_temp_high, day_temp_low_param=day_temp_low, day_humidity_param=day_humidity)

def build_response_text(data):
    city = data['city']['name']
    days = []
    payload_text = """
---
### Weather forecast for {location} next 7 days
| Day | Description | High | Low | Humidity |
|:---------------------------|:------------------------------------|:--------|:--------|:--------|\n""".format(location=city)
    for day in data['list']:
        payload_text += get_day_weather_line(day)
    payload_text += "---"
    return payload_text

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
