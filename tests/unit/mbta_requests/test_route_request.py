import unittest
from mbta_api.mbta_requests.route_options import RouteOptions
from mbta_api.mbta_requests.route_request import RouteRequest

class TestRouteRequest(unittest.TestCase):

    def test_get(self):
        route_options = RouteOptions(page_limit=1, filter_type='0,1')
        route_request = RouteRequest()
        routes_is_more = route_request.get(route_options)
        returned_routes:dict = routes_is_more[0]
        is_more:bool = routes_is_more[1]
        self.assertGreaterEqual(len(returned_routes),1)
        self.assertEqual(returned_routes.get('Red').id, 'Red')

    def test_getAll(self):
        route_options = RouteOptions(filter_type='0,1')
        route_request = RouteRequest()
        routes_is_more = route_request.get(route_options)
        returned_routes:dict = routes_is_more[0]
        is_more:bool = routes_is_more[1]
        self.assertGreaterEqual(len(returned_routes),7)
        self.assertEqual(returned_routes.get('Red').id, 'Red')
