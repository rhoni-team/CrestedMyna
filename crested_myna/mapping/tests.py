from django.test import TestCase
from data_loading.read_data.read_world_shp import ReadWorldShp
from mapping.views import GetCountriesPolygonsWithACRecords
from django.core.management import call_command


# Test the ReadWorldShp class
class TestGetCountriesPolygons(TestCase):
    """ Tests for the GetCountriesPolygons class """

    @staticmethod
    def setUpTestData():
        """Set up the test data"""
        call_command('migrate', 'data_loading')

    def setUp(self):
        """ Set up the test """
        self.inst_get_countries_pol = GetCountriesPolygonsWithACRecords()

    def test_number_of_countries_with_ac_records(self):
        """ Test the number of countries polygons with AC records """
        countries = self.inst_get_countries_pol.get_countries_polygons_with_ac_records()
        self.assertEqual(len(countries), 24)
