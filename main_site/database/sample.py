from pymongo import MongoClient

client = MongoClient()
db = client.test
"""
sample_data = {
	"city": "Sunnyvale",
	"country": "US", 
	"temperature": {
		"low": 63,
		"average":72,
		"high": 84
	},
	"humidity %": 79
}
db.weather_sample.insert(sample_data)
"""
cursor = db.sample_weather.find()
for document in cursor:
	print('City: ', document['location'])
	print('Average temperature: ', document['temp'])
	print('Will have sun: ', document['will_have_sun'])
