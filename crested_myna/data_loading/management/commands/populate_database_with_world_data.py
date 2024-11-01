"""
This module contains the command to populate the WorldBorder
with the data from the world shapefile.
"""

import os
from data_loading.models import WorldBorder
from data_loading.models import ACRecord
from data_loading.load import run
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count


directory = os.getcwd()

class Command(BaseCommand):
    """
    Command to populate the WorldBorder table with the data from the world shapefile.
    """

    help = "Populate WorldBorder table with world shapefile"

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        try:
            # add shapefile to database
            self.save_world_shp_in_database()
            self.stdout.write(self.style.SUCCESS('Successfully populated the database with the world shapefile'))

            # add ac_count to world shapefile
            ac_count_dict = self.get_ac_count_for_countries()

            for country in WorldBorder.objects.all():
                country.ac_count = ac_count_dict.get(country.iso2, 0)
                country.save()

            self.stdout.write(self.style.SUCCESS('Successfully added ac_count to world shapefile'))

        except WorldBorder.DoesNotExist:
            raise CommandError('WorldBorder object does not exist')
        
    def save_world_shp_in_database(self):
        """ Save the world shapefile in the database """
        run()

    def get_ac_count_for_countries(self) -> dict:
        """ Get the ac_count for each country """
        counts_by_country = ACRecord.objects.values("country_code").annotate(ac_count=Count("country_code"))
        ac_count_dict = {item['country_code']: item['ac_count'] for item in counts_by_country}
        return ac_count_dict
