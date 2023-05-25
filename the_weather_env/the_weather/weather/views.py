from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):

    cities = City.objects.all() #return all the cities in the database
    
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    
    form = CityForm()
    weather_data = []
    for city in cities:
            appid = ''
            city = str(city)
            urlGeo = 'http://api.openweathermap.org/geo/1.0/direct?q='+ city +'&appid=' + appid
            city_locaton = requests.get(urlGeo).json()
            lat = str((city_locaton[0]['lat']))
            lon = str((city_locaton[0]['lon']))
            urlWeather = 'https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&units=metric'+'&appid='+appid
            city_weather = requests.get(urlWeather).json()


            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)



    context = {'weather_data' : weather_data, 'form' :form}


 
    
    return render(request, 'weather/index.html', context) #returns the index.html template







