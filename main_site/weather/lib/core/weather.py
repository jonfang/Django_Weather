import pyowm, json
owm = pyowm.OWM('538cea50e439653ca98c8a8c1f5b6f8b')

#make a class next time to add in self to each instanace
#locations=['Sunnyvale, US', 'San Jose, US', 'Palo Alto, US', 'San Francisco, US', 'Oakland, US', 'Berkeley, US']
#attributes=['temp', 'temp_min', 'temp_max', 'humidity']
#weather_data = {} #a dict of dict to store weather data

class Weather:
	def __init__(self):
		"""constructor"""
		self.sample = 'This is the weather main app from weather module'

	def main(self):
		"print the sample string"
		#print(self.sample)

	def collect_weather_data(self,locations, attributes, weather_data):
		for city in locations:
		#get weather data from owm API
			weather = owm.weather_at_place(city)
			temperature_1 = weather.get_weather()
			temperature = temperature_1.get_temperature('fahrenheit')
			humidity_1 = weather.get_weather()
			humidity = humidity_1.get_humidity()
		#forecast data from owm API
			forecast = owm.daily_forecast(city)
			sun = forecast.will_have_sun()
			rain = forecast.will_have_rain()
			clouds = forecast.will_have_clouds()
			snow = forecast.will_have_snow()
		#for each city, store its weather attributes into weather_data
			weather_data[city] = {}
			for attribute in attributes:
				if attribute == 'humidity':
					weather_data[city][attribute] = str(humidity)
				elif 'will_have' in attribute:
					if'sun' in attribute:
						weather_data[city][attribute] = str(sun)
					elif 'rain' in attribute:
						weather_data[city][attribute] = str(rain)
					elif 'clouds' in attribute:
						weather_data[city][attribute] = str(clouds)
					else:
					#snow
						weather_data[city][attribute] = str(snow)
				else:
					weather_data[city][attribute] = str(temperature[attribute])

	def print_weather_data(self, weather_data):
		"""Print Weather data"""
		count = 1
		for city, weather in weather_data.items():
			print(count,city,'===>')
			for attr, value in weather.items():
				print(str(attr) + ':'+  str(value))
			count = count + 1

	def convert_to_json(self, weather_data):
		"""Convert weather data into readable json format"""
		row = {}
		for city, weather in weather_data.items():
			row['location'] = city
			row.update({attr: value for attr, value in weather.items()})
			#print(row)
			j = json.dumps(row)
			print(j)
	sample = 'Hello World!'
'''
		#save this for unit testing
		print(city + '===>')
		print('Current temperature:' + str(temperature['temp']))
		print('Minimum temperature:' + str(temperature['temp_min']))
		print('Maximum temperature:' + str(temperature['temp_max']))
		print('Humidity:' + str(humidity) + '%')
'''
