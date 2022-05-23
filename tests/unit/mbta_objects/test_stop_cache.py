import unittest
from mbta_api.mbta_objects.stop import Stop
from mbta_api.mbta_objects.stop_cache import StopCache
from tests.example_data import test_stops_json, test_stops_cache



class TestStopCache(unittest.TestCase):


    def test_insertStop(self):
        stop_cache = StopCache()
        for stop_json in test_stops_json:
            stop = Stop(stop_json)
            stop_cache.insertStop(stop)
        redblue = stop_cache.stops['red-blue']
        bluegrey = stop_cache.stops['blue-grey']
        greybrown = stop_cache.stops['grey-brown']
        
        self.assertEqual(redblue.routes[0], 'red')
        self.assertEqual(redblue.routes[1], 'blue')
        self.assertEqual(bluegrey.routes[0], 'blue')
        self.assertEqual(bluegrey.routes[1], 'grey')
        self.assertEqual(greybrown.routes[0], 'grey')
        self.assertEqual(greybrown.routes[1], 'brown')


    def test_findJunctions(self):
        junctions = test_stops_cache.findJunctions()
        self.assertEqual(junctions, junctions | {
            'red-blue': test_stops_cache.stops['red-blue']
            ,'blue-grey': test_stops_cache.stops['blue-grey']
            ,'grey-brown': test_stops_cache.stops['grey-brown']
        })


if __name__ == '__main__':
    unittest.main()