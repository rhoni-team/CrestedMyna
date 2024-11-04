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
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    iso2 = models.CharField("2 Digit ISO", max_length=2)
    latitude = models.FloatField(validators=[MinValueValidator(-90), 
                                             MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), 
                                              MaxValueValidator(180)])
    ac_count = models.IntegerField(null=True)
    geom = models.MultiPolygonField()

    def __str__(self):
        """String representation of the ACRecord model."""
        return self.name
