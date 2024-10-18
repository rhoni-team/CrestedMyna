"""
This module contains the command to populate the ACRecord table with the data from the csv file.
"""

import os

from data_analysis.models import ACRecord as Record
from data_analysis.read_data.read_csv import RecordsFromCsv
from django.core.management.base import BaseCommand, CommandError

directory = os.getcwd()

class Command(BaseCommand):
    """
    Command to populate the ACRecord table with the data from the csv file.
    """

    help = "Populate ACRecord table with ebird cleaned data from csv"

    def create_ACRecord_objects(self):
        """
        Create the ACRecord objects.
        """
        inst_read_csv = RecordsFromCsv()
        data = inst_read_csv.get_rows_list()
        AC_objects = [Record(**row) for row in data]
        return AC_objects

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        try:
            AC_objects = self.create_ACRecord_objects()
            Record.objects.bulk_create(AC_objects)
            self.stdout.write(self.style.SUCCESS('Successfully populated the database with AC records'))
        except Record.DoesNotExist:
            raise CommandError('Record does not exist')
