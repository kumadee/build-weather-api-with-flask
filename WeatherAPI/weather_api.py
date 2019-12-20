import datetime as dt
import json
import math

from flask import Flask, request, Response, Blueprint

from WeatherAPI.models import db, Location, Weather

from flask_restful import Resource, Api, fields, marshal

from WeatherAPI.parsers import WeatherRequestParser, WeatherGetParser, LocationParser, WeatherEraseParser, TemperatureGetParser, PreferredLocationsParser
from WeatherAPI.marshallers import resource_fields, temp_fields, no_temp_fields, location_fields, preferred_location_details

weather_bp = Blueprint('WeatherAPI', __name__)

weatherapi = Api(weather_bp)


class WeatherList(Resource):

    def get(self):
        

    def post(self):
        


class WeatherErase(Resource):

    def delete(self):
        



    
class LocationTemp(Resource):

    def get(self):
        

    
class PreferredLocationsAPI(Resource):
    
    def get(self):
        
        
weatherapi.add_resource(WeatherAPI, '/weather')
weatherapi.add_resource(WeatherEraseAPI, '/erase')
weatherapi.add_resource(TemperatureAPI, '/weather/temperature')
weatherapi.add_resource(PreferredLocationsAPI, '/weather/locations')

