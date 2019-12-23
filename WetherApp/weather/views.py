from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    apikey = 'a93f229c93a7e698d7b035927b6af85e'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+apikey
    #city = 'Donetsk'

    if(request.method== 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm() #для очистки формы от предыдущего запроса


    cities = City.objects.all()
    all_cities = []
    for city in cities:
        print(city.name)
        res = requests.get(url.format(city.name)).json()
        print (res)
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    # city_info = {
    #     'city': city,
    #     'temp': res["main"]['temp'],
    #     'icon': res["weather"][0]["icon"]
    # }

    context = {'all_info': all_cities, 'form': form}
    #print (context)

    return render(request, 'weather/index.html', context) #шаблоны по умолчанию ищутся в папке templates
