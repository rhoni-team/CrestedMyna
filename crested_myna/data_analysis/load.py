""" Module to load the world shapefile into the database 
This module uses the LayerMapping class from django.contrib.gis.utils 
to load the world shapefile into the database.
Only the relevant attributes columns are loaded into the database.
"""
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder
import data_analysis


# map object with the selected columns
worldborder_mapping = {
    'iso2': 'ISO2',
    'name': 'NAME',
    'area': 'AREA',
    'latitude': 'LAT',
    'longitude': 'LON',
    'geom': 'MULTIPOLYGON',
}

# path to the world shapefile
WORLD_SHP_PATH = Path(data_analysis.__file__).resolve().parent / "data" / "countries_data" / "world_shp" / "TM_WORLD_BORDERS-0.3.shp"


def run(verbose=True):
    """ run function to load the world shapefile into the database """
    lm = LayerMapping(WorldBorder, WORLD_SHP_PATH, worldborder_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
