import unittest
from mbta_api.mbta_requests.config import api_key
class TestConfig(unittest.TestCase):

    def test_api_key(self):
        self.assertIsNotNone(api_key)
