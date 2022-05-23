import io
import unittest
from unittest.mock import patch 
from mbta_api.views.route_view import RouteView
from tests.example_data import test_routes_cache_completed



class TestRouteView(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_showRoutes(self, mock_stdout):
        route_view = RouteView(test_routes_cache_completed)
        route_view.showRoutes()
        self.assertEqual(mock_stdout.getvalue(), 
        '''Listing Cached Routes
<id>: <name>
-----------------
red: Red Line
blue: Blue Line
brown: Brown Line
grey: Grey Line
'''
        )

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_showRouteMaxStops(self, mock_stdout):
        route_view = RouteView(test_routes_cache_completed)
        route_view.showRouteMaxStops()
        self.assertEqual(mock_stdout.getvalue(), 'Route with Most Stops: Blue Line - 3 Stops\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_showRouteMinStops(self, mock_stdout):
        route_view = RouteView(test_routes_cache_completed)
        route_view.showRouteMinStops()
        self.assertEqual(mock_stdout.getvalue(), 'Route with Least Stops: Red Line - 2 Stops\n')

    def test_findRoute(self):
        route_view = RouteView(test_routes_cache_completed)
        self.assertEqual(route_view.findRoute('red').id, 'red')
        self.assertEqual(route_view.findRoute('none'), None)


if __name__ == '__main__':
    unittest.main() 