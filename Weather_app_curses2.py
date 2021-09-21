import requests
import json
import os.path
import curses
import time
import datetime
from weather_map_class import WeatherOneCallAPI

lat_c = str(47.684052)
lon_c = str(17.635099)

API_key = ""

try:
    screen = curses.initscr()
except curses.error():
    print("An erro occured:" + curses.error())
    exit()

curses.curs_set(0)

def _map(value, input_start, input_end, output_start, output_end):
    output = output_start + ((output_end - output_start) / (input_end - input_start)) * (value - input_start)
    return output


def main():
    
    weather = WeatherOneCallAPI()
    weather.init(apikey=API_key, lat=lat_c, lon=lon_c)
    weather.getData()

    while (True):
        if (datetime.datetime.now().minute % 10 == 0) and (datetime.datetime.now().second == 0):
            weather.getData()
            time.sleep(0.1)
            screen.clear()

        num_rows, num_cols = screen.getmaxyx()

        screen.addstr(0, 0, "Weather_app_curses.py")
        screen.addstr(0, num_cols - 20, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        

        screen.addstr(1, 0, ("Rows: " + str(num_rows)))
        screen.addstr(2, 0, ("Cols: " + str(num_cols)))

        screen.addstr(4, 0, "Updates: " + str(weather.update_times))

        #-----------------------

        screen.addstr(1, 30, str(weather.lat()) + "°")
        screen.addstr(2, 30, str(weather.lon()) + "°")
        screen.addstr(3, 30, str(weather.timezone()))
        screen.addstr(4, 30, str(weather.timezone_offset()))

        screen.addstr(0, 50, "Current:")
        screen.addstr(1, 50, "Ido:\t\t" + str(datetime.datetime.fromtimestamp(weather.current.dt())))
        screen.addstr(2, 50, "Napfelkelte:\t" + str(datetime.datetime.fromtimestamp(weather.current.sunrise()).strftime('%H:%M:%S')))
        screen.addstr(3, 50, "Napnyugta:\t" + str(datetime.datetime.fromtimestamp(weather.current.sunset()).strftime('%H:%M:%S')))


        screen.addstr(4, 50, "Hofok:\t" + str(weather.current.temp()) + " °C")
        screen.addstr(5, 50, "Erzet:\t" + str(weather.current.feels_like()) + " °C")
        screen.addstr(6, 50, "Legnyomas:\t" + str(weather.current.pressure()) + " Hpa")
        screen.addstr(7, 50, "Paratartalom:\t" + str(weather.current.humidity()) + " %")
        screen.addstr(8, 50, "Harmatpont:\t" + str(weather.current.dew_point()) + " °C")
        screen.addstr(9, 50, "Eso:\t\t" + str(weather.current.rain()) + " ")
        screen.addstr(10, 50, "Felho:\t" + str(weather.current.clouds()) + " ")
        screen.addstr(11, 50, "Szel:\t\t" + str(weather.current.wind_speed()) + " km/h")
        screen.addstr(12, 50, "Szelirany:\t" + str(weather.current.wind_deg()) + "° " + weather.windString(weather.current.wind_deg()))
    
        wind_speed_max = 0
        wind_speed_min = 0

        for wind_speed in range(12):
            if(weather.hourly.wind_speed(wind_speed) > wind_speed_max):
                wind_speed_max = weather.hourly.wind_speed(wind_speed)

        for o in range(12):
            screen.addstr(o, 100, str(weather.hourly.wind_speed(o)) + ('  km/h' if (100 * weather.hourly.wind_speed(o) % 10 == 0) else  ' km/h'))
            value = int(_map(weather.hourly.wind_speed(o), wind_speed_min, wind_speed_max, 0, 20))    
            for x in range(value):
                screen.addstr(o, 110 + x, "#")

        #-----------------------
    
        curses.napms(100)
        screen.refresh()

try:
    main()
except KeyboardInterrupt:
    print("Window ended.")
finally:
    curses.endwin()
