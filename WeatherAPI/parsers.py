from flask_restful import reqparse
from WeatherAPI import validators
    
# Define the following Parsers
# NOTE: Use the custom 'datestring' validator defined in 'WeatherAPI/validators.py' for validating input date string.
# 1. WeatherRequestParser : It parses the values of input fields-  'id', 'date', 'temperature', and 'location', present in a JSON entry
## The value of 'location' field is another json entry, whose values are parsed by LocationParser
class WeatherRequestParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type = int, required = True, location = 'json')
        self.parser.add_argument('date', type = validators.datestring, location = 'json')
        self.parser.add_argument('temperature', type = list, location = 'json')
        self.parser.add_argument('location', type = LocationParser(self.parser), location = 'json')

# 2. LocationParser : It parses the values of input fields - 'lat', 'lon', 'city', and 'state', passed to 'location' field of weather JSON input entry.
class LocationParser:
    def __init__(self, parser):
        self.parser = parser
        self.parser.add_argument('lat', type = float, location = 'json')
        self.parser.add_argument('lon', type = float, location = 'json')
        self.parser.add_argument('city', location = 'json')
        self.parser.add_argument('state', location = 'json')

# 3. WeatherGetParser : It parses the values of input fields - 'date', 'lat' and 'lon', present in a query string.
class WeatherGetParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('date', type = validators.datestring)
        self.parser.add_argument('lat', type = float)
        self.parser.add_argument('lon', type = float)

# 4. WeatherEraseParser : It parses the values of input fields - 'start', 'end', 'lat' and 'lon', present in  a query string
class WeatherEraseParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('start', type = validators.datestring)
        self.parser.add_argument('end', type = validators.datestring)
        self.parser.add_argument('lat', type = float)
        self.parser.add_argument('lon', type = float)

# 5. TemperatureGetParser : It parses the values of input fields - 'start', 'end', present in  a query string
class TemperatureGetParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('start', type = validators.datestring)
        self.parser.add_argument('end', type = validators.datestring)

# 6. PreferredLocationsParser : It parses the values of input fields - 'date', 'lat' and 'lon', present in  a query string
class PreferredLocationsParser(WeatherGetParser):
    pass
