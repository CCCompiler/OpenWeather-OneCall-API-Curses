import weather_map_class
import sys
import json
import os

lat_c = str(47.684052)
lon_c = str(17.635099)

API_key = "9833e2889bbc43ab32f6365a7cfb4947"

weather = weather_map_class.WeatherOneCallAPI()
weather.init(apikey=API_key, lat=lat_c, lon=lon_c)
weather.getData()
with open('testdata.json', 'w') as f:
    json.dump(weather.data, f)

f_size = os.path.getsize('testdata.json')

print(f_size, 'bytes')
