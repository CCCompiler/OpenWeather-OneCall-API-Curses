import requests
from pprint import pprint

lat = str(47.684052)
lon = str(17.635099)

API_key = ""
base_url = "https://api.openweathermap.org/data/2.5/onecall?"

Final_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + API_key 

data = requests.get(Final_url).json()

pprint(data)
