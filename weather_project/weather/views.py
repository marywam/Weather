from django.shortcuts import render
from .models import WeatherData

def get_weather(request):
    # Fetch all weather data from the database
    weather_data = WeatherData.objects.all()

    # Create a context dictionary to pass data to the template
    context = {
        'weather_data': weather_data
    }

    # Render the template with the context data
    return render(request, 'index.html', context)


