import datetime as dt
import json
import math

from flask import Flask, request, Response, Blueprint

from WeatherAPI.models import db, Location, Weather, db_insert

from flask_restful import Resource, Api, fields, marshal_with

from WeatherAPI.parsers import WeatherRequestParser, WeatherGetParser, LocationParser, WeatherEraseParser, TemperatureGetParser, PreferredLocationsParser
from WeatherAPI.marshallers import resource_fields, temp_fields, no_temp_fields, location_fields, preferred_location_fields

weather_bp = Blueprint('WeatherAPI', __name__)

weatherapi = Api(weather_bp)


class WeatherAPI(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = WeatherRequestParser().parser.parse_args()
        return Weather.query.join(Location).filter_by(
            Location.lat = args.get('lat'), 
            Location.lon = args.get('lon'), 
        )

    def post(self):
        args = WeatherRequestParser().parser.parse_args()
        weather = Weather()
        for key, value in args.iteritems():
            if key == 'id':
                weather.id = value
            elif key == 'date':
                weather.date = value
            elif key == 'temperature':
                weather.temperature = value
            elif key == 'location':
                _location = Location()
                _location.lat = value.get('lat')
                _location.lon = value.get('lon') 
                _location.city = value.get('city')
                _location.state = value.get('state')
                weather.location = _location
        db_insert(weather)
        return


class WeatherEraseAPI(Resource):

    def delete(self):
        pass


class TemperatureAPI(Resource):
    @marshal_with(temp_fields)
    def get(self):
        pass


class PreferredLocationsAPI(Resource):
    @marshal_with(preferred_location_fields)
    def get(self):
        pass


weatherapi.add_resource(WeatherAPI, '/weather')
weatherapi.add_resource(WeatherEraseAPI, '/erase')
weatherapi.add_resource(TemperatureAPI, '/weather/temperature')
weatherapi.add_resource(PreferredLocationsAPI, '/weather/locations')
