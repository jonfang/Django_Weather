from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#import python app package
from .lib.core import weather
from .lib.core import main
#import MongoDB module
from pymongo import MongoClient
client = MongoClient()
db = client.test

# Create your views here.
def get_weather():
    """helper method to get weather data"""
    return {'locations':main.locations}

def index(request):
    """View the main index page for weather forecasting"""
    context = get_weather()
    return render(request, 'weather/index.html', context)

def search(request):
    "Search and return requested data"""
    if 'q' in request.GET:
        forecast={}
        cursor = db.sample_weather.find()
        city_list = list(document['location'] for document in cursor)
        q = request.GET['q']
        if q in city_list: #if the requested city is in the city list
            cursor = db.sample_weather.find({'location': q})
            for document in cursor:
                city = 'City: ' +  document['location']
                temp = '\nAverage temperature(F): ' + document['temp'] 
                temp += '\n Minimum temperature(F): ' + document['temp_min']
                temp += '\n Maximum temperature(F): ' + document['temp_max']
                temp += '\n Humidity(%): ' + document['humidity']
                forecast['sun'] = document['will_have_sun']
                forecast['rain'] = document['will_have_snow']
                forecast['clouds'] = document['will_have_clouds']
                forecast['snow'] = document['will_have_snow']
            message = ''
            message += city + temp
        else:
            context = get_weather()
            context.update({'error':True})
            return render(request, 'weather/index.html', context)
    else:
        context = get_weather()
        context.update({'error':True})
        return render(request, 'weather/index.html', {'error': True})
    context =  {'message':message, 'forecast':forecast}
    return render(request, 'weather/result.html', context)

