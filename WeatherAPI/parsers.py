from flask_restful import reqparse
from WeatherAPI import validators
    
# Define the following Parsers
# NOTE: Use the custom 'datestring' validator defined in 'WeatherAPI/validators.py' for validating input date string.
# 1. WeatherRequestParser : It parses the values of input fields-  'id', 'date', 'temperature', and 'location', present in a JSON entry
## The value of 'location' field is another json entry, whose values are parsed by LocationParser

# 2. LocationParser : It parses the values of input fields - 'lat', 'lon', 'city', and 'state', passed to 'location' field of weather JSON input entry.

# 3. WeatherGetParser : It parses the values of input fields - 'date', 'lat' and 'lon', present in a query string.

# 4. WeatherEraseParser : It parses the values of input fields - 'start', 'end', 'lat' and 'lon', present in  a query string
# 5. TemperatureGetParser : It parses the values of input fields - 'start', 'end', present in  a query string

# 6. PreferredLocationsParser : It parses the values of input fields - 'date', 'lat' and 'lon', present in  a query string

