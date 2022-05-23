import io
import unittest
from unittest.mock import patch 
from mbta_api.views.stop_view import StopView
from tests.example_data import test_stops_cache



class TestStopView(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_showStops(self, mock_stdout):
        stop_view = StopView(test_stops_cache)
        stop_view.showStops()
        self.assertEqual(mock_stdout.getvalue(), 
        '''Listing Cached Stops
<id>: <name>
-----------------
red-0: Red Start
red-blue: Red Blue Junction
blue-0: Blue middle
blue-grey: Blue Grey Junction
grey-brown: Grey Brown Junction
brown-0: Brown Start
'''
        )

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_showJunctions(self, mock_stdout):
        stop_view = StopView(test_stops_cache)
        stop_view.showJunctions()
        self.assertEqual(mock_stdout.getvalue(), 
        '''Listing Junctions
<id>: <name>
-----------------
red-blue: Red Blue Junction - ['red', 'blue']
blue-grey: Blue Grey Junction - ['blue', 'grey']
grey-brown: Grey Brown Junction - ['grey', 'brown']
'''
        )


    def test_findStop(self):
        stop_view = StopView(test_stops_cache)
        self.assertEqual(stop_view.findStop('blue-grey').id, 'blue-grey')
        self.assertEqual(stop_view.findStop('none'), None)



if __name__ == '__main__':
    unittest.main() 