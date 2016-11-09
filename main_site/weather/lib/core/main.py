import weather #weather app module 
import os

#input parameters, comment this out to get locations from a file
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'city_names.txt')
locations = []
with open(file_path) as data_file:
	for city in data_file:
		locations.append(city.rstrip())
#comment this out to manually provide locations
#locations=['Sunnyvale, US', 'San Jose, US', 'Palo Alto, US', 'Mountain View, US', 'Los Gatos, US', 'Los Altos, US', 'Fremont, US', 'San Francisco, US', 'Oakland, US', 'Berkeley, US']
attributes=['temp', 'temp_min', 'temp_max', 'humidity', 'will_have_sun', 'will_have_rain', 'will_have_clouds', 'will_have_snow']
weather_data = {} #a dict of dict to store weather data


if __name__ == "__main__":
	x = weather.Weather() 
	x.main()
	#print(locations)
	x.collect_weather_data(locations, attributes, weather_data)
	#x.print_weather_data(weather_data)
	x.convert_to_json(weather_data)
