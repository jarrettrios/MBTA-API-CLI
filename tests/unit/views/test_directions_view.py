import io
import unittest
from unittest.mock import patch 
from mbta_api.views.directions_view import DirectionsView
from tests.example_data import test_routes_cache_completed



class TestDirectionsView(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_showRouteBetweenStops(self, mock_stdout):
        directions_view = DirectionsView(test_routes_cache_completed)
        directions_view.showRouteBetweenStops(
            test_routes_cache_completed.routes['red'].stops['red-blue']
            ,test_routes_cache_completed.routes['brown'].stops['brown-0']
        )
        self.assertEqual(mock_stdout.getvalue(), 'Blue Line ---> Grey Line ---> Brown Line\n')



if __name__ == '__main__':
    unittest.main()