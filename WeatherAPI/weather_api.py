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


class WeatherAPI(Resource):

    def get(self):
        pass

    def post(self):
        pass


class WeatherEraseAPI(Resource):

    def delete(self):
        pass


class TemperatureAPI(Resource):

    def get(self):
        pass


class PreferredLocationsAPI(Resource):

    def get(self):
        pass


weatherapi.add_resource(WeatherAPI, '/weather')
weatherapi.add_resource(WeatherEraseAPI, '/erase')
weatherapi.add_resource(TemperatureAPI, '/weather/temperature')
weatherapi.add_resource(PreferredLocationsAPI, '/weather/locations')
