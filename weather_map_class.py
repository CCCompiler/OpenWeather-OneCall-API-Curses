import requests
import json


class WeatherOneCallAPI():
    """Main Class"""

#    def __init__ (self, data):
#        self.data = data
#        self.current = self.Current(self.data)
#        self.minutely = self.Minutely(self.data)
#        self.hourly = self.Hourly(self.data)
#        self.daily = self.Daily(self.data)

    def init(self, apikey=None, lon=0, lat=0):
        __url = "https://api.openweathermap.org/data/2.5/onecall?" + "lat=" + lat + "&lon=" + lon + "&appid=" + apikey + "&units=metric"
        self.url = __url
        self.update_times = 0

    def getData(self):
        self.data = requests.get(self.url).json()
        self.current = self.Current(self.data)
        self.minutely = self.Minutely(self.data)
        self.hourly = self.Hourly(self.data)
        self.daily = self.Daily(self.data)
        self.update_times += 1

    def windString(self, value):
        # 0 = É, 45 = ÉK, 90 = K, 135 = DK, 180 = D, 225 = DNY, 270 = NY, 315 = ÉNY, 360 = É
        __e_l = 0
        __e_k = 45
        __k = 90
        __d_k = 135
        __d = 180
        __d_ny = 225
        __ny = 270
        __e_ny = 315
        __e_h = 360
        
        if (value < ((__e_k - __e_l)/2)) or (value > ((__e_h - __e_ny)/2)):
            return 'Észak'
        elif (value < ((__k - __e_k)/2)) or (value > ((__e_k - __e_l)/2)):
            return 'Észak-Kelet'
        elif (value < ((__d_k - __k)/2)) or (value > ((__k - __e_k)/2)):
            return 'Kelet'
        elif (value < ((__d - __d_k)/2)) or (value > ((__d_k - __k)/2)):
            return 'Dél-Kelet'
        elif (value < ((__d_ny - __d)/2)) or (value > ((__d - __d_k)/2)):
            return 'Dél'
        elif (value < ((__ny - __d_ny)/2)) or (value > ((__d_ny - __d)/2)):
            return 'Dél-Nyugat'
        elif (value < ((__e_ny - __ny)/2)) or (value > ((__ny - __d_ny)/2)):
            return 'Nyugat'
        elif (value < ((__e_h - __e_ny)/2)) or (value > ((__e_ny - __ny)/2)):
            return 'Észak-Nyugat'


    def lat(self):
        return self.data['lat']
    
    def lon(self):
        return self.data['lon']

    def timezone(self):
        return self.data['timezone']
    
    def timezone_offset(self):
        return self.data['timezone_offset']

    """Current Weather Class"""

    class Current:
        def __init__(self, data):
            self.data = data
            self.weather = self.CurrentWeather(self.data)
            
        def dt(self):
            return self.data['current']['dt']
        
        def sunrise(self):
            return self.data['current']['sunrise']
        
        def sunset(self):
            return self.data['current']['sunset']
        
        def temp(self):
            return self.data['current']['temp']

        def feels_like(self):
            return self.data['current']['feels_like']

        def pressure(self):
            return self.data['current']['pressure']

        def humidity(self):
            return self.data['current']['humidity']

        def dew_point(self):
            return self.data['current']['dew_point']
        
        def uvi(self):
            return self.data['current']['uvi']

        def clouds(self):
            return self.data['current']['clouds']

        def visibility(self):
            return self.data['current']['visibility']

        def wind_speed(self):
            return self.data['current']['wind_speed']
        
        def wind_deg(self):
            return self.data['current']['wind_deg']
        
        class CurrentWeather:
            def __init__ (self, data):
                self.data = data
            
            def id(self):
                return self.data['current']['weather'][0]['id']

            def main(self):
                return self.data['current']['weather'][0]['main']

            def description(self):
                return self.data['current']['weather'][0]['description']
            
            def icon(self):
                return self.data['current']['weather'][0]['icon']

        def rain(self):
            try:
                return self.data['current']['rain']['1h']
            except KeyError:
                return 0

    class Minutely:
        def __init__ (self, data):
            self.data = data
        
        def dt(self, num):
            return self.data['minutely'][num]['dt']

        def precipitation(self, num):
            return self.data['minutely'][num]['precipitation']
    
    class Hourly:
        def __init__ (self, data):
            self.data = data
            self.weather = self.HourlyWeather(self.data)
        
        def dt(self, num):
            return self.data['hourly'][num]['dt']
        
        def temp(self, num):
            return self.data['hourly'][num]['temp']

        def feels_like(self, num):
            return self.data['hourly'][num]['feels_like']
        
        def pressure(self, num):
            return self.data['hourly'][num]['pressure']

        def humidity(self, num):
            return self.data['hourly'][num]['humidity']
        
        def dew_point(self, num):
            return self.data['hourly'][num]['dew_point']
        
        def uvi(self, num):
            return self.data['hourly'][num]['uvi']

        def clouds(self, num):
            return self.data['hourly'][num]['clouds']
        
        def visibility(self, num):
            return self.data['hourly'][num]['visibility']
        
        def wind_speed(self, num):
            return self.data['hourly'][num]['wind_speed']

        def wind_deg(self, num):
            return self.data['hourly'][num]['wind_deg']

        class HourlyWeather:
            def __init__ (self, data):
                self.data = data
            
            def id(self, num):
                return self.data['hourly'][num]['weather'][0]['id']

            def main(self, num):
                return self.data['hourly'][num]['weather'][0]['main']

            def description(self, num):
                return self.data['hourly'][num]['weather'][0]['description']
            
            def icon(self, num):
                return self.data['hourly'][num]['weather'][0]['icon']

        def pop(self, num):
            return self.data['hourly'][num]['pop']

        def rain(self, num):
            try:
                return self.data['hourly'][num]['rain']['1h']
            except KeyError:
                return 0
    class Daily:
        def __init__ (self, data):
            self.data = data
            self.temp = self.DailyTemp(self.data)
            self.feels_like = self.DailyFeels_like(self.data)
            self.weather = self.DailyWeather(self.data)
        
        def dt(self, num):
            return self.data['daily'][num]['dt']

        def sunrise(self, num):
            return self.data['daily'][num]['sunrise']

        def sunset(self, num):
            return self.data['daily'][num]['sunset']

        class DailyTemp:
            def __init__ (self, data):
                self.data = data
            
            def day(self, num):
                return self.data['daily'][num]['temp']['day']
            
            def min(self, num):
                return self.data['daily'][num]['temp']['min']

            def max(self, num):
                return self.data['daily'][num]['temp']['max']

            def night(self, num):
                return self.data['daily'][num]['temp']['night']

            def eve(self, num):
                return self.data['daily'][num]['temp']['eve']

            def morn(self, num):
                return self.data['daily'][num]['temp']['morn']
        
        class DailyFeels_like:
            def __init__ (self, data):
                self.data = data

            def day(self, num):
                return self.data['daily'][num]['feels_like']['day']
            
            def night(self, num):
                return self.data['daily'][num]['feels_like']['night']

            def eve(self, num):
                return self.data['daily'][num]['feels_like']['eve']

            def morn(self, num):
                return self.data['daily'][num]['feels_like']['morn']
        
        def pressure(self, num):
            return self.data['daily'][num]['pressure']
        
        def humidity(self, num):
            return self.data['daily'][num]['humidity']

        def dew_point(self, num):
            return self.data['daily'][num]['dew_point']

        def wind_speed(self, num):
            return self.data['daily'][num]['wind_speed']

        def wind_deg(self, num):
            return self.data['daily'][num]['wind_deg']
        
        class DailyWeather:
            def __init__ (self, data):
                self.data = data

            def id(self, num):
                return self.data['daily'][num]['weather'][0]['id']

            def main(self, num):
                return self.data['daily'][num]['weather'][0]['main']

            def description(self, num):
                return self.data['daily'][num]['weather'][0]['description']

            def icon(self, num):
                return self.data['daily'][num]['weather'][0]['icon']

        def clouds(self, num):
            return self.data['daily'][num]['clouds']

        def pop(self, num):
            return self.data['daily'][num]['pop']

        def rain(self, num):
            try:
                return self.data['daily'][num]['rain']
            except KeyError:
                return 0

        def uvi(self, num):
            return self.data['daily'][num]['uvi']
            

        
        


    
    def printAll(self):
        print("All available things:")
        print('')
        print(f"Get lat: {self.lat()}")
        print('')
        print(f"Get lon: {self.lon()}")
        print('')
        print(f"Get timezone: {self.timezone()}")
        print('')
        print(f"Get timezone_offset: {self.timezone_offset()}")
        print('')
        print(f"Get current.dt: {self.current.dt()}")
        print('')
        print(f"Get current.sunrise: {self.current.sunrise()}")
        print('')
        print(f"Get current.temp: {self.current.temp()}")
        print('')
        print(f"Get current.feels_like: {self.current.feels_like()}")
        print('')
        print(f"Get current.pressure: {self.current.pressure()}")
        print('')
        print(f"Get current.humidity: {self.current.humidity()}")
        print('')
        print(f"Get current.dew_point: {self.current.dew_point()}")
        print('')
        print(f"Get current.uvi: {self.current.uvi()}")
        print('')
        print(f"Get current.clouds: {self.current.clouds()}")
        print('')
        print(f"Get current.visibility: {self.current.visibility()}")
        print('')
        print(f"Get current.wind_speed: {self.current.wind_speed()}")
        print('')
        print(f"Get current.wind_deg: {self.current.wind_deg()}")
        print('')
        print(f"Get current.weather.id: {self.current.weather.id()}")
        print('')
        print(f"Get current.weather.main: {self.current.weather.main()}")
        print('')
        print(f"Get current.weather.description: {self.current.weather.description()}")
        print('')
        print(f"Get current.weather.icon: {self.current.weather.icon()}")
        print('')
        print(f"Get current.rain: {self.current.rain()}")
        print('')
        print(f"Get minutely.dt(0): {self.minutely.dt(0)}")
        print('')
        print(f"Get minutely.precipitation(0): {self.minutely.precipitation(0)}")
        print('')
        print(f"Get hourly.dt(0): {self.hourly.dt(0)}")
        print('')
        print(f"Get hourly.temp(0): {self.hourly.temp(0)}")
        print('')
        print(f"Get hourly.feels_like(0): {self.hourly.feels_like(0)}")
        print('')
        print(f"Get hourly.pressure(0): {self.hourly.pressure(0)}")
        print('')
        print(f"Get hourly.humidity(0): {self.hourly.humidity(0)}")
        print('')
        print(f"Get hourly.dew_point(0): {self.hourly.dew_point(0)}")
        print('')
        print(f"Get hourly.uvi(0): {self.hourly.uvi(0)}")
        print('')
        print(f"Get hourly.clouds(0): {self.hourly.clouds(0)}")
        print('')
        print(f"Get hourly.visibility(0): {self.hourly.visibility(0)}")
        print('')
        print(f"Get hourly.wind_speed(0): {self.hourly.wind_speed(0)}")
        print('')
        print(f"Get hourly.wind_deg(0): {self.hourly.wind_deg(0)}")
        print('')
        print(f"Get hourly.weather.id(0): {self.hourly.weather.id(0)}")
        print('')
        print(f"Get hourly.weather.main(0): {self.hourly.weather.main(0)}")
        print('')
        print(f"Get hourly.weather.description(0): {self.hourly.weather.description(0)}")
        print('')
        print(f"Get hourly.weather.icon(0): {self.hourly.weather.icon(0)}")
        print('')
        print(f"Get hourly.pop(0): {self.hourly.pop(0)}")
        print('')
        print(f"Get hourly.rain(0): {self.hourly.rain(0)}")
        print('')
        print(f"Get daily.dt(0): {self.daily.dt(0)}")
        print('')
        print(f"Get daily.sunrise(0): {self.daily.sunrise(0)}")
        print('')
        print(f"Get daily.sunset(0): {self.daily.sunset(0)}")
        print('')
        print(f"Get daily.temp.day(0): {self.daily.temp.day(0)}")
        print('')
        print(f"Get daily.temp.min(0): {self.daily.temp.min(0)}")
        print('')
        print(f"Get daily.temp.max(0): {self.daily.temp.max(0)}")
        print('')
        print(f"Get daily.temp.night(0): {self.daily.temp.night(0)}")
        print('')
        print(f"Get daily.temp.eve(0): {self.daily.temp.eve(0)}")
        print('')
        print(f"Get daily.temp.morn(0): {self.daily.temp.morn(0)}")
        print('')
        print(f"Get daily.feels_like.day(0): {self.daily.feels_like.day(0)}")
        print('')
        print(f"Get daily.feels_like.night(0): {self.daily.feels_like.night(0)}")
        print('')
        print(f"Get daily.feels_like.eve(0): {self.daily.feels_like.eve(0)}")
        print('')
        print(f"Get daily.feels_like.morn(0): {self.daily.feels_like.morn(0)}")
        print('')
        print(f"Get daily.pressure(0): {self.daily.pressure(0)}")
        print('')
        print(f"Get daily.humidity(0): {self.daily.humidity(0)}")
        print('')
        print(f"Get daily.dew_point(0): {self.daily.dew_point(0)}")
        print('')
        print(f"Get daily.wind_speed(0): {self.daily.wind_speed(0)}")
        print('')
        print(f"Get daily.wind_deg(0): {self.daily.wind_deg(0)}")
        print('')
        print(f"Get daily.weather.id(0): {self.daily.weather.id(0)}")
        print('')
        print(f"Get daily.weather.main(0): {self.daily.weather.main(0)}")
        print('')
        print(f"Get daily.weather.description(0): {self.daily.weather.description(0)}")
        print('')
        print(f"Get daily.weather.icon(0): {self.daily.weather.icon(0)}")
        print('')
        print(f"Get daily.clouds(0): {self.daily.clouds(0)}")
        print('')
        print(f"Get daily.pop(0): {self.daily.pop(0)}")
        print('')
        print(f"Get daily.rain(0): {self.daily.rain(0)}")
        print('')
        print(f"Get daily.uvi(0): {self.daily.uvi(0)}")
        