""" Module to read the world shapefile """
from pathlib import Path
from django.contrib.gis.gdal import DataSource
import data_loading


WORLD_SHP_PATH = Path(data_loading.__file__).resolve().parent / "data" / "countries_data" / "world_shp" / "TM_WORLD_BORDERS-0.3.shp"


class ReadWorldShp:
    """ Class to read the world shapefile """

    def __init__(self, world_shp_path=WORLD_SHP_PATH):
        self.world_shp_path = world_shp_path

    def read_world_shp_as_data_source(self):
        """ Read the world shapefile as a DataSource """
        self.world_shp_data = DataSource(self.world_shp_path)
