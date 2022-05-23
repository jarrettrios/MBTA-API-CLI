from mbta_requests.route_options import RouteOptions
from mbta_objects.route import Route
from .config import api_key
import requests
import json

class RouteRequest():
    '''
    An object that wraps the MBTA API's Route request. It allows for the abstraction of interacting with the API.
    '''

    def __init__(self, route_options:RouteOptions = RouteOptions()):
        self.route_options = route_options
    
    def get(self, route_options:RouteOptions = None) -> tuple:
        '''
        Gets the list of routes for the configured parameters.

        Returns: Tuple, index 0 is the dict of routes, index 1 is a boolean representing whether there is another page of data. 
        '''
        if route_options is not None:
            self.route_options = route_options
        payload = {}
        if self.route_options.page_offset:
            payload['page[offset]'] = self.route_options.page_offset
        if self.route_options.page_limit:
            payload['page[limit]'] = self.route_options.page_limit
        if self.route_options.sort:
            payload['sort'] = self.route_options.sort
        if self.route_options.fields_route:
            payload['fields[route]'] = self.route_options.fields_route
        if self.route_options.include:
            payload['include'] = self.route_options.include
        if self.route_options.filter_stop:
            payload['filter[stop]'] = self.route_options.filter_stop
        if self.route_options.filter_type:
            payload['filter[type]'] = self.route_options.filter_type
        if self.route_options.filter_direction_id:
            payload['filter[direction_id]'] = self.route_options.filter_direction_id
        if self.route_options.filter_date:
            payload['filter[date]'] = self.route_options.filter_date
        if self.route_options.filter_id:
            payload['filter[id]'] = self.route_options.filter_id
        if api_key:
            payload['api_key]'] = api_key

        response = requests.get('https://api-v3.mbta.com/routes', params=payload)

        routes = {}
        json_response = json.loads(response.text)
        json_routes = json_response['data']

        # Check to see if there is "next" link, to see if there are further pages of data
        is_more = False
        try:
            if 'next' in json_response['links']:
                is_more = True
        except KeyError:
            pass

        for json_route in json_routes:
            routes[json_route['id']] = Route(json_route)

        return (routes, is_more)
    
    def getAll(self, route_options:RouteOptions = None) -> dict:
        '''
        Gets the dict of all routes for the configured parameters. Will start at offset 0.
        '''
        # Preserve old offset
        if route_options is not None:
            self.route_options = route_options

        old_page_offset = self.route_options.page_offset
        self.route_options.page_offset = 0
        routes, is_next = self.get()
        while is_next:
            self.route_options.page_offset = self.route_options.page_offset + 1
            new_routes, is_next = self.get()
            routes = {**routes, **new_routes}
        return routes
    