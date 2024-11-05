""" Tests for the data_analysis app """
from django.test import TestCase
from pathlib import Path
import data_loading
from data_loading.read_data.read_world_shp import ReadWorldShp


WORLD_SHP_PATH = Path(data_loading.__file__).resolve().parent / "data" / "countries_data" / "world_shp" / "TM_WORLD_BORDERS-0.3.shp"


# Test the ReadWorldShp class
class TestReadWorldShp(TestCase):
    """ Tests for the ReadWorldShp class """

    def setUp(self):
        """ Set up the test """
        self.utils_read_world_shp = ReadWorldShp(world_shp_path=WORLD_SHP_PATH)

    def test_read_world_shp(self):
        """ Test the read_world_shp method by counting its features """
        self.utils_read_world_shp.read_world_shp_as_data_source()
        polygon_layer = self.utils_read_world_shp.world_shp_data[0]
        self.assertEqual(len(polygon_layer), 246)

