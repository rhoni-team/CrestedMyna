""" Module to load the world shapefile and the cities shapefile into the database
This module uses the LayerMapping class from django.contrib.gis.utils
to load the shapefiles into the database.
Only the relevant attributes columns are loaded.
"""
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
import data_loading
from data_loading.models import Country, CitiesIMB, CitiesEsri


# map object with the selected columns
country_mapping = {
    'iso2': 'ISO2',
    'name': 'NAME',
    'geom': 'MULTIPOLYGON',
}

cities_imb_mapping = {
    'genc1': 'GENC1',
    'city_name': 'Name',
    'population': 'Pop',
    'lat': 'Lat',
    'lon': 'Lon',
    'geom': 'POINT',
}

cities_esri_mapping = {
    'fips_cntry': 'FIPS_CNTRY',
    'city_name': 'CITY_NAME',
    'population': 'POP',
    'geom': 'POINT',
}

# path to the world shapefile
WORLD_SHP_PATH = Path(data_loading.__file__).resolve().parent / "data" / \
    "countries_data" / "world_shp" / "TM_WORLD_BORDERS-0.3.shp"

CITIES_IMB_PATH = Path(data_loading.__file__).resolve().parent / "data" / \
    "cities_data" / "world_cities_imb" / "Cities.shp"

CITIES_ESRI_PATH = Path(data_loading.__file__).resolve().parent / "data" / \
    "cities_data" / "world_cities_esri" / "World_Cities.shp"


def run(verbose=True):
    """ run function to load shapefiles """

    # load world shapefile
    lm = LayerMapping(Country, WORLD_SHP_PATH, country_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
    
    # load imb cities
    lm = LayerMapping(CitiesIMB, CITIES_IMB_PATH, cities_imb_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

    # load esri cities
    lm = LayerMapping(CitiesEsri, CITIES_ESRI_PATH, cities_esri_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
