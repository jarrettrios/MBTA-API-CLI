from mbta_api.mbta_objects.stop import Stop
from tests.example_data import test_stop
import unittest

class TestStop(unittest.TestCase):
    def testInstantation(self):
        stop = Stop(test_stop)
        self.assertEqual(stop.id, 'test id')
        self.assertEqual(stop.address, 'test address')
        self.assertEqual(stop.at_street, 'test at_street')
        self.assertEqual(stop.description, 'test description')
        self.assertEqual(stop.latitude, 'test latitude')
        self.assertEqual(stop.location_type, 'test location_type')
        self.assertEqual(stop.municipality, 'test municipality')
        self.assertEqual(stop.name, 'test name')
        self.assertEqual(stop.on_street, 'test on_street')
        self.assertEqual(stop.platform_code, 'test platform_code')
        self.assertEqual(stop.platform_name, 'test platform_name')
        self.assertEqual(stop.vehicle_type, 'test vehicle_type')
        self.assertEqual(stop.wheelchair_boarding, 'test wheelchair_boarding')
        self.assertEqual(stop.routes[0], 'test route')
        self.assertEqual(stop.child_stops[0], 'test child_stops')
        self.assertEqual(stop.connecting_stops[0], 'test connecting_stops')


if __name__ == '__main__':
    unittest.main()