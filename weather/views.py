import requests
import os
from django.shortcuts import render
from datetime import datetime

def index(request):
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = os.getenv('WEATHER_API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
                'date': datetime.now().strftime('%A, %d %B %Y'),
                'time': datetime.now().strftime('%I:%M %p'),
            }
        else:
            error = "City not found! Please try again."
    
    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error': error
    })