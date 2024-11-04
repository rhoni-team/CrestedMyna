""" Module to load the world shapefile into the database 
This module uses the LayerMapping class from django.contrib.gis.utils 
to load the world shapefile into the database.
Only the relevant attributes columns are loaded into the database.
"""
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Country
import data_loading


# map object with the selected columns
country_mapping = {
    'iso2': 'ISO_A2',
    'name': 'FORMAL_EN',
    'geom': 'MULTIPOLYGON',
}

# path to the world shapefile
WORLD_SHP_PATH = Path(data_loading.__file__).resolve().parent / "data" / "countries_data" / "world_shp" / "WB_countries_Admin0_10m.shp"


def run(verbose=True):
    """ run function to load the world shapefile into the database """
    lm = LayerMapping(Country, WORLD_SHP_PATH, country_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
