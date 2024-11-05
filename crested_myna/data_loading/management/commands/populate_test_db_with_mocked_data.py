import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from data_loading.models import ACRecord as Record
from data_loading.read_data.read_csv import RecordsFromCsv
from django.core.management.base import BaseCommand, CommandError


path_mocked_csv = "./data_loading/data/ebird_data/mocked_crested_myna_records.csv"

# Set random seed for reproducibility
np.random.seed(42)

# Number of records
n_records = 175

# Create mock data
mock_data = {
    'checklist_id': [f'M{str(i).zfill(8)}' for i in range(n_records)],
    'latitude': np.random.uniform(14.0, 39.0, n_records),
    'longitude': np.random.uniform(97.0, 122.0, n_records),
    'country_code': np.random.choice(['TW', 'CN', 'HK', 'PH', 'MY', 'JP', 'MO', 'PT'], n_records,
                                     p=[0.4, 0.2, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05]),
    'observation_date': [(datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 150))) for _ in range(n_records)],
    'observation_count': np.random.choice(np.concatenate([np.array([np.nan]), np.arange(1, 51)]), n_records),
    'time_observations_started': [f"{str(np.random.randint(5, 19)).zfill(2)}:{str(np.random.randint(0, 60)).zfill(2)}:00" for _ in range(n_records)],
    'duration_minutes': np.random.choice(np.concatenate([np.array([np.nan]), np.arange(5, 401)]), n_records),
}

# Create DataFrame
df = pd.DataFrame(mock_data)

# Add country, state and state_code based on country_code
country_mapping = {
    'TW': ('Taiwan', ['Taipei City', 'Kinmen County', 'New Taipei City', 'Taichung City'], ['TW-TPE', 'TW-KIN', 'TW-TPQ', 'TW-TXG']),
    'CN': ('China', ['Shanghai', 'Beijing', 'Guangdong', 'Fujian'], ['CN-31', 'CN-11', 'CN-44', 'CN-35']),
    'HK': ('Hong Kong', ['Hong Kong'], ['HK-']),
    'PH': ('Philippines', ['Manila', 'Laguna', 'Rizal'], ['PH-00', 'PH-LAG', 'PH-RIZ']),
    'MY': ('Malaysia', ['Sabah', 'Pulau Pinang'], ['MY-12', 'MY-07']),
    'JP': ('Japan', ['Osaka', 'Tokyo'], ['JP-27', 'JP-13']),
    'MO': ('Macau', ['Macau'], ['MO-']),
    'PT': ('Portugal', ['Lisboa', 'Setúbal'], ['PT-11', 'PT-15'])
}

df['country'] = df['country_code'].map(lambda x: country_mapping[x][0])
df['state'] = df.apply(lambda x: np.random.choice(country_mapping[x['country_code']][1]), axis=1)
df['state_code'] = df.apply(lambda x: np.random.choice(country_mapping[x['country_code']][2]), axis=1)

# Save to CSV
df.to_csv(path_mocked_csv, index=False)


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
        inst_read_csv = RecordsFromCsv(path_csv=path_mocked_csv)
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
            self.stdout.write(self.style.SUCCESS(
                'Successfully populated the database with MOCKED CRESTED MYNA records'))
        except Record.DoesNotExist:
            raise CommandError('Record does not exist')
