#This class is used to test PYOWM functionalities
from pyowm import OWM
owm = OWM('538cea50e439653ca98c8a8c1f5b6f8b')
obs = owm.weather_at_place('London,uk')
w = obs.get_weather()
#get current weather data
print("Get temperature: ", w.get_temperature())
#get forecast information
fc = owm.daily_forecast('San Jose, us')
print("Have sun?: ", fc.will_have_sun())
print("Have rain?: ", fc.will_have_rain())
print("Have fog?: ", fc.will_have_fog())
print("Have clouds? ", fc.will_have_clouds())
