import unittest
from mbta_api.mbta_requests.stop_options import StopOptions
from mbta_api.mbta_requests.stop_request import StopRequest

class TestStopRequest(unittest.TestCase):

    def test_get(self):
        stop_options = StopOptions(page_limit=1, filter_id='place-brntn')
        stop_request = StopRequest()
        stops_is_more = stop_request.get(stop_options)
        returned_stops:dict = stops_is_more[0]
        is_more:bool = stops_is_more[1]
        print(returned_stops)
        self.assertGreaterEqual(len(returned_stops),1)
        self.assertEqual(returned_stops.get('place-brntn').id, 'place-brntn')

    def test_getAll(self):
        stop_options = StopOptions(filter_route='Red')
        stop_request = StopRequest(stop_options)
        stops_is_more = stop_request.get()
        returned_stops:dict = stops_is_more[0]
        is_more:bool = stops_is_more[1]
        self.assertGreaterEqual(len(returned_stops),22)
        self.assertEqual(returned_stops.get('place-brntn').id, 'place-brntn')
