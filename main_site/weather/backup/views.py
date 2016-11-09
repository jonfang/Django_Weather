from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#from .lib import main 
from .lib.core import weather
from .lib.core import main

#mongoDB importing
from pymongo import MongoClient
client = MongoClient()
db = client.test

# Create your views here.
def get_weather():
	"""helper method to get weather data"""
	#x = weather.Weather()
	#x.main()
	#x.collect_weather_data(main.locations, main.attributes, main.weather_data)
	#print('debug===>:', main.locations)
	#x.convert_to_json(main.weather_data)
	#return {'locations':main.locations, 'weather_data':main.weather_data}
	return {'locations':main.locations}

def index(request):
	#main.main()
	#main.collect_weather_data(main.locations)
	#main.print_weather_data(main.locations, main.weather_data)
	#x = weather.Weather()
	#x.main()
	#x.collect_weather_data(main.locations, main.attributes, main.weather_data)
	#x.convert_to_json(main.weather_data)
	#context = {'locations':main.locations, 'weather_data':main.weather_data}
	context = get_weather()
	return render(request, 'weather/index.html', context)

#search_form htm to test out searching functionality
#def search_form(request):
    #return render(request, 'weather/search_form.html')

def search(request):
	#check if the input parameter is in the list
    #cursor = db.sample_weather.find()
    #city_list = list(document['location'] for document in cursor)
    #if 'q' in city_list:
       # message = 'You searched for: %r and it is in the list' % request.GET['q']
    #cursor = db.sample_weather.find({'location':'Palo Alto, US'})
    #for document in cursor:
         #city = 'City: ' +  document['location']
         #temp = 'Average temperature: ' + document['temp']
    if 'q' in request.GET:
        forecast={}
        cursor = db.sample_weather.find()
        city_list = list(document['location'] for document in cursor)
        q = request.GET['q']
        if q in city_list:
            #correct pass
            cursor = db.sample_weather.find({'location': q})
            for document in cursor:
                city = 'City: ' +  document['location']
                temp = '\nAverage temperature(F): ' + document['temp'] 
                temp += '\n Minimum temperature(F): ' + document['temp_min']
                temp += '\n Maximum temperature(F): ' + document['temp_max']
                temp += '\n Humidity(%): ' + document['humidity']
            #test icon hiding/display
                forecast['sun'] = document['will_have_sun']
                forecast['rain'] = document['will_have_snow']
                forecast['clouds'] = document['will_have_clouds']
                forecast['snow'] = document['will_have_snow']
            #message = 'You searched for: %r and it is a valid city:' % q 
            message = ''
            message += city + temp
            #test icon hiding/display
        else:
            #error and return
            context = get_weather()
            context.update({'error':True})
            return render(request, 'weather/index.html', context)
    else:
	#error and return
        context = get_weather()
        context.update({'error':True})
        return render(request, 'weather/index.html', {'error': True})
    #return HttpResponse(message)
    context =  {'message':message, 'forecast':forecast}
    return render(request, 'weather/result.html', context)

    #return render(request, 'weather/result.html', {'message':message, 'icons':"hello"})
