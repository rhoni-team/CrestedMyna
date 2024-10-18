"""Django models for the data analysis app."""
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ACRecord(models.Model):
    """
    Model for the AC records.
    """
    checklist_id = models.CharField(max_length=100)
    latitude = models.FloatField(validators=[MinValueValidator(-90), 
                                             MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), 
                                              MaxValueValidator(180)])
    country_code = models.CharField(max_length=2)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    state_code = models.CharField(max_length=150)
    observation_date = models.DateField(null=False)
    year = models.IntegerField(null=True)
    observation_count = models.IntegerField(null=True, blank=True)
    time_observations_started = models.TimeField(null=True)
    duration_minutes = models.IntegerField(null=True)

    class Meta:
        """Meta options for the ACRecord model."""
        ordering = ['country', 'year']

    def __str__(self):
        """String representation of the ACRecord model."""
        return f'{self.country_code} _ {self.year}'
