from WeatherAPI.models import Location
from flask_restful import fields, marshal

## Define the following marshallers below
# 1. 'location_details' : It defines the output formation of a location entry
# 2. 'resource_fields' :
# 3. 'temp_fields' :
# 4. 'no_temp_fields' :
# 5. 'preferred_location_details' :

location_details = {
    'lat': fields.Float,
    'lon': fields.Float,
    'city': fields.String,
    'state': fields.String
}

resource_fields = {
    'id': fields.Integer,
    'date': fields.DateTime(dt_format='iso8601'),
    'location': fields.Nested(location_details)
    'temperature': fields.List(fields.Float)
}

temp_fields = {}

no_temp_fields = {}

preferred_location_details = {}
