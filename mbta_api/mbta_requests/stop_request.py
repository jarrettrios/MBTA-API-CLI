from mbta_requests.stop_options import StopOptions
from mbta_objects.stop import Stop
from .config import api_key
import requests
import json

class StopRequest():
    '''
    An object that wraps the MBTA API's Stop request. It allows for the abstraction of interacting with the API.
   '''

    def __init__(self, stop_options:StopOptions = StopOptions()):
        self.stop_options = stop_options

    def get(self, stop_options:StopOptions = None) -> tuple:
        '''
        Gets the list of routes for the configured parameters.

        Returns: Tuple, index 0 is the dict of routes, index 1 is a boolean representing whether there is another page of data. 
        '''
        if stop_options is not None:
            self.stop_options = stop_options
        payload = {}
        if self.stop_options.page_offset:
            payload['page[offset]'] = self.stop_options.page_offset
        if self.stop_options.page_limit:
            payload['page[limit]'] = self.stop_options.page_limit
        if self.stop_options.sort:
            payload['sort'] = self.stop_options.sort
        if self.stop_options.fields_stop:
            payload['fields[stop]'] = self.stop_options.fields_stop
        if self.stop_options.include:
            payload['include'] = self.stop_options.include
        if self.stop_options.page_offset:
            payload['filter[date]'] = self.stop_options.filter_date
        if self.stop_options.filter_direction_id:
            payload['filter[direction_id]'] = self.stop_options.filter_direction_id
        if self.stop_options.filter_latitude:
            payload['filter[latitude]'] = self.stop_options.filter_latitude
        if self.stop_options.filter_longitude:
            payload['filter[longitude]'] = self.stop_options.filter_longitude
        if self.stop_options.filter_radius:
            payload['filter[radius]'] = self.stop_options.filter_radius
        if self.stop_options.filter_id:
            payload['filter[id]'] = self.stop_options.filter_id
        if self.stop_options.filter_route_type:
            payload['filter[route_type]'] = self.stop_options.filter_route_type
        if self.stop_options.filter_route:
            payload['filter[route]'] = self.stop_options.filter_route
        if self.stop_options.filter_service:
            payload['filter[service]'] = self.stop_options.filter_service
        if self.stop_options.filter_location_type:
            payload['filter[location_type]'] = self.stop_options.filter_location_type
        if api_key:
            payload['api_key]'] = api_key

        response = requests.get('https://api-v3.mbta.com/stops', params=payload)

        stops = {}
        json_response = json.loads(response.text)
        json_stops = json_response['data']

        # Check to see if there is "next" link, to see if there are further pages of data
        is_more = False
        try:
            if 'next' in json_response['links']:
                is_more = True
        except KeyError:
            pass

        for json_stop in json_stops:
            stops[json_stop['id']] = Stop(json_stop)

        return (stops, is_more)
    
    def getAll(self, stop_options:StopOptions = None) -> dict:
        '''
        Gets the dict of all routes for the configured parameters. Will start at offset 0.
        '''
        # Preserve old offset
        if stop_options is not None:
            self.stop_options = stop_options
        old_page_offset = self.stop_options.page_offset
        self.stop_options.page_offset = 0
        stops, is_next = self.get()
        while is_next:
            self.stop_options.page_offset = self.stop_options.page_offset + 1
            new_stops, is_next = self.get()
            stops = {**stops, **new_stops}
        return stops
    