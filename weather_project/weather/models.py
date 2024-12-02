#This line imports the models module from Django's database layer. The models module provides the necessary classes and functions to define the structure of your database tables.
from django.db import models    

#In Django, a model is a Python class that represents a database table. By inheriting from models.Model, WeatherData becomes a Django model.
class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

# The __str__ method provides a readable string representation of the WeatherData object, showing the city name and temperature.
    def __str__(self):
        return f"{self.city} - {self.temperature}°C"

