# -*- coding: utf-8 -*-

import unittest
import os
from datetime import datetime
from pyowm.constants import DEFAULT_API_KEY
from pyowm.webapi25.configuration25 import parsers
from pyowm.webapi25.owm25 import OWM25


class IntegrationTestsUVIndexAPI30(unittest.TestCase):

    __owm = OWM25(parsers, os.getenv('OWM_API_KEY', DEFAULT_API_KEY))

    def test_uvindex_around_coords(self):
        """
        Test feature: get UV index around geo-coordinates.
        """
        u = self.__owm.uvindex_around_coords(45, 9)
        self.assertIsNotNone(u)
        self.assertIsNotNone(u.get_value())
        self.assertIsNotNone(u.get_reception_time())
        self.assertIsNotNone(u.get_location())

    def test_uvindex_forecast_around_coords(self):
        """
        Test feature: get UV index forecast around geo-coordinates.
        """
        uv_list = self.__owm.uvindex_forecast_around_coords(45, 9)
        self.assertIsInstance(uv_list, list)
        for item in uv_list:
            self.assertIsNotNone(item.get_value())
            self.assertIsNotNone(item.get_reception_time())
            self.assertIsNotNone(item.get_location())

    def test_uvindex_history_around_coords(self):
        """
        Test feature: get UV index history around geo-coordinates.
        """
        start = datetime(2017, 6, 21)
        end = datetime(2017, 6, 27)
        uv_list = self.__owm.uvindex_history_around_coords(37.7, -122.37,
                                                           start,
                                                           end=end)
        self.assertIsInstance(uv_list, list)
        for item in uv_list:
            self.assertIsNotNone(item.get_value())
            self.assertIsNotNone(item.get_reception_time())
            self.assertIsNotNone(item.get_location())


if __name__ == "__main__":
    unittest.main()