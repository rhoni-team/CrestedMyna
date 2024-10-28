"""
This module contains the command to populate the WorldBorder
with the data from the world shapefile.
"""

import os
from data_analysis.models import WorldBorder
from data_analysis.load import run
from django.core.management.base import BaseCommand, CommandError


directory = os.getcwd()

class Command(BaseCommand):
    """
    Command to populate the WorldBorder table with the data from the world shapefile.
    """

    help = "Populate WorldBorder table with world shapefile"

    def save_world_shp_in_database(self):
        """ Save the world shapefile in the database """
        run()

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        try:
            self.save_world_shp_in_database()
            self.stdout.write(self.style.SUCCESS('Successfully populated the database with the world shapefile'))
        except WorldBorder.DoesNotExist:
            raise CommandError('WorldBorder object does not exist')
