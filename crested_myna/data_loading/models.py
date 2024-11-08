"""Django models for the data analysis app."""
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.gis.db import models


class ACRecord(models.Model):
    """
    Model for the AC records.
    """
    checklist_id = models.CharField(max_length=100)
    latitude = models.FloatField(validators=[MinValueValidator(-90),
                                             MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180),
                                              MaxValueValidator(180)])
    location = ArrayField(models.FloatField(), size=2, null=True, blank=True)
    country_code = models.CharField(max_length=2)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    state_code = models.CharField(max_length=150)
    observation_date = models.DateField(null=False)
    year = models.IntegerField(null=True)
    observation_count = models.IntegerField(null=True, blank=True)
    time_observations_started = models.TimeField(null=True)
    duration_minutes = models.IntegerField(null=True)
    geom = models.PointField(null=True)

    class Meta:
        """Meta options for the ACRecord model."""
        ordering = ['country', 'year']

    def __str__(self):
        """String representation of the ACRecord model."""
        return f'{self.country_code} _ {self.year}'


class Country(models.Model):
    """
    Model for the world borders.
    """
    name = models.CharField(max_length=120, null=True, default='Unnamed Country')
    iso2 = models.CharField("2 Digit ISO", max_length=2, null=True, blank=True)
    geom = models.MultiPolygonField()

    def __str__(self):
        """String representation of the Country model."""
        return self.name if self.name else "Unnamed Country"


class CitiesIMB(models.Model):
    """
    Model for the world borders.
    """
    genc1 = models.CharField(max_length=10, null=True)
    city_name = models.CharField(max_length=250, null=True)
    population = models.IntegerField(null=True)
    lat = models.FloatField(validators=[MinValueValidator(-90),
                                             MaxValueValidator(90)], null=True)
    lon = models.FloatField(validators=[MinValueValidator(-180),
                                              MaxValueValidator(180)], null=True)
    geom = models.PointField(null=True)

    def __str__(self):
        """String representation of the Country model."""
        return self.city_name if self.city_name else "Unnamed City"

class CitiesEsri(models.Model):
    """
    Model for the world borders.
    """
    fips_cntry = models.CharField(max_length=10, null=True)
    city_name = models.CharField(max_length=250, null=True)
    population = models.IntegerField(null=True)
    lat = models.FloatField(validators=[MinValueValidator(-90),
                                             MaxValueValidator(90)], null=True)
    lon = models.FloatField(validators=[MinValueValidator(-180),
                                              MaxValueValidator(180)], null=True)
    geom = models.PointField(null=True)

    def __str__(self):
        """String representation of the Country model."""
        return self.city_name if self.city_name else "Unnamed City"
    
class Cities(models.Model):
    """
    Model for the cities.
    """
    city_name = models.CharField(max_length=250, null=True)
    population = models.IntegerField(null=True)
    lat = models.FloatField(validators=[MinValueValidator(-90),
                                             MaxValueValidator(90)], null=True)
    lon = models.FloatField(validators=[MinValueValidator(-180),
                                              MaxValueValidator(180)], null=True)
    geom = models.PointField(null=True, srid=3857)


class CountrySimplified(models.Model):
    """ 
    Model for the world borders simplified after applying ST_Simplify with a 0.01 tolerance.
    """
    name = models.CharField(max_length=120, null=True, default='Unnamed Country')
    iso2 = models.CharField("2 Digit ISO", max_length=2, null=True, blank=True)
    simple_geom = models.MultiPolygonField(null=True)

    def __str__(self):
        """String representation of the Country model."""
        return self.name if self.name else "Unnamed Country"


class CountryWithACRecord(models.Model):
    """ Country model with only the countries that have AC records. """
    name = models.CharField(max_length=120, null=True, default='Unnamed Country')
    iso2 = models.CharField("2 Digit ISO", max_length=2, null=True, blank=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90),
                                             MaxValueValidator(90)],
                                 null=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180),
                                              MaxValueValidator(180)],
                                  null=True)
    tot_birds_count = models.IntegerField(null=True, default=1)
    tot_observations_events = models.IntegerField(null=True)
    is_exotic = models.BooleanField(null=True)
    geom = models.MultiPolygonField()

    def __str__(self):
        """String representation of the CountryWithACRecord model."""
        return self.name
