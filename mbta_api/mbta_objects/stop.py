class Stop():
    '''
    A python object, representing the Stop JSONObject from the MBTA API V3.0
    '''
    def __init__(self, json_stop:dict):
        
        self.id = json_stop.get('id')
        
        attributes = json_stop.get('attributes')
        relationships = json_stop.get('relationships')

        self.address = attributes.get('address')
        self.at_street = attributes.get('at_street')
        self.description = attributes.get('description')
        self.latitude = attributes.get('latitude')
        self.location_type = attributes.get('location_type')
        self.longitude = attributes.get('longitude')
        self.municipality = attributes.get('municipality')
        self.name = attributes.get('name')
        self.on_street = attributes.get('on_street')
        self.platform_code = attributes.get('platform_code')
        self.platform_name = attributes.get('platform_name')
        self.vehicle_type = attributes.get('vehicle_type')
        self.wheelchair_boarding = attributes.get('wheelchair_boarding')
        self.routes = []
        self.routes.append(relationships.get('route',{'data':{}}).get('data').get('id'))

        self.child_stops = []
        if 'child_stops' in relationships:
            for stop in relationships.get('child_stops').get('data'):
                self.child_stops.append(stop.get('id'))

        self.connecting_stops = []
        if 'connecting_stops' in relationships:
            for stop in relationships.get('connecting_stops').get('data'):
                self.connecting_stops.append(stop.get('id'))

