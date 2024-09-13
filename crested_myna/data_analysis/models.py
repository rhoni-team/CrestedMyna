"""Django models for the data analysis app."""
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def get_year(instance):
    """Get the year from the observation date."""
    return instance.observation_date.year


class ACRecord(models.Model):
    """
    Model for the AC records.
    """
    observation_count = models.IntegerField(null=True)
    country = models.CharField(max_length=150)
    country_code = models.CharField(max_length=2)
    state = models.CharField(max_length=150)
    state_code = models.CharField(max_length=150)
    latitude = models.FloatField(validators=[MinValueValidator(-90), 
                                             MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), 
                                              MaxValueValidator(180)])
    observation_date = models.DateField(null=False)
    year = models.IntegerField(default=get_year)

    class Meta:
        """Meta options for the ACRecord model."""
        ordering = ['country', 'year']

    def __str__(self):
        """String representation of the ACRecord model."""
        return f'{self.country_code} _ {self.year}'
