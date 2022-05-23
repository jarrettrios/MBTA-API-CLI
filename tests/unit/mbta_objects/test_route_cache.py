import unittest
from tests.example_data import test_routes_cache, test_stops_cache



class TestRoute(unittest.TestCase):

    def test_updateRouteStops(self):
        test_routes_cache.updateRouteStops(test_stops_cache)
        red = test_routes_cache.routes['red']
        self.assertEqual(red.stops['red-0'].id, 'red-0')
        self.assertEqual(red.stops['red-blue'].id, 'red-blue')

        blue = test_routes_cache.routes['blue']
        self.assertEqual(blue.stops['red-blue'].id, 'red-blue')
        self.assertEqual(blue.stops['blue-0'].id, 'blue-0')
        self.assertEqual(blue.stops['blue-grey'].id, 'blue-grey')

        grey = test_routes_cache.routes['grey']
        self.assertEqual(grey.stops['blue-grey'].id, 'blue-grey')
        self.assertEqual(grey.stops['grey-brown'].id, 'grey-brown')

        brown = test_routes_cache.routes['brown']
        self.assertEqual(brown.stops['grey-brown'].id, 'grey-brown')
        self.assertEqual(brown.stops['brown-0'].id, 'brown-0')

    def test_updateRouteConnections(self):
        test_routes_cache.updateRouteConnections(test_stops_cache)

        red = test_routes_cache.routes['red']
        blue = test_routes_cache.routes['blue']
        grey = test_routes_cache.routes['grey']
        brown = test_routes_cache.routes['brown']

        self.assertEqual(red.connections[0], blue)
        self.assertEqual(blue.connections[0], red)
        self.assertEqual(blue.connections[1], grey)
        self.assertEqual(grey.connections[0], blue)
        self.assertEqual(grey.connections[1], brown)
        self.assertEqual(brown.connections[0], grey)

    def test_routeWithMaxStops(self):
        test_routes_cache.updateRouteStops(test_stops_cache)
        blue = test_routes_cache.routes['blue']
        self.assertEqual(test_routes_cache.routeWithMaxStops(), blue)
        
    def test_routeWithMinStops(self):
        test_routes_cache.updateRouteStops(test_stops_cache)
        red = test_routes_cache.routes['red']
        self.assertEqual(test_routes_cache.routeWithMinStops(), red)

if __name__ == '__main__':
    unittest.main()