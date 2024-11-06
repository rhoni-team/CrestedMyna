""" Tests for the mapping app """
from django.test import TestCase
from django.core.management import call_command
from mapping.views.views_get_data import GetCountriesPolygonsWithACRecords


# Test the ReadWorldShp class
class TestGetCountriesPolygons(TestCase):
    """ Tests for the GetCountriesPolygons class """

    @staticmethod
    def setUpTestData():
        """Set up the test data"""
        call_command('migrate', 'data_loading', '0001_initial', '--fake')
        call_command('populate_test_db_with_mocked_data')
        call_command('populate_database_with_world_data')

    def setUp(self):
        """ Set up the test """
        self.inst_get_countries_pol = GetCountriesPolygonsWithACRecords()

    def test_number_of_countries_with_ac_records(self):
        """ Test the number of countries polygons with AC records """
        countries = self.inst_get_countries_pol.get_countries_polygons_with_ac_records()
        self.assertEqual(len(countries), 24)
