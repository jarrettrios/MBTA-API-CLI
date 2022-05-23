from mbta_api.mbta_objects.route import Route
from tests.example_data import test_route
import unittest

class TestRoute(unittest.TestCase):
    def test_instantation(self):
        route = Route(test_route)
        self.assertEqual(route.id, 'test id')
        self.assertEqual(route.color, 'test color')
        self.assertEqual(route.description, 'test description')
        self.assertEqual(route.direction_destinations, 'test direction_destinations')
        self.assertEqual(route.direction_names, 'test direction_names')
        self.assertEqual(route.fare_class, 'test fare_class')
        self.assertEqual(route.long_name, 'test long_name')
        self.assertEqual(route.short_name, 'test short_name')
        self.assertEqual(route.sort_order, 'test sort_order')
        self.assertEqual(route.text_color, 'test text_color')
        self.assertEqual(route.type, 'test type')


if __name__ == '__main__':
    unittest.main()