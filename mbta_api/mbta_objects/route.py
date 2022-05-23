class Route():
    '''
    A python object, representing the Route JSONObject from the MBTA API V3.0.
    '''

    def __init__(self,  json_route:dict):
        attributes = json_route.get('attributes')
        self.id = json_route.get('id')
        self.color = attributes.get('color')
        self.description = attributes.get('description')
        self.direction_destinations = attributes.get('direction_destinations')
        self.direction_names = attributes.get('direction_names')
        self.fare_class = attributes.get('fare_class')
        self.long_name = attributes.get('long_name')
        self.short_name = attributes.get('short_name')
        self.sort_order = attributes.get('sort_order')
        self.text_color = attributes.get('text_color')
        self.type = attributes.get('type')
        self.stops = {}
        self.connections = []
