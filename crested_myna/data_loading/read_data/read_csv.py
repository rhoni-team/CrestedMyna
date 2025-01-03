"""
This module contains the class RecordsFromCsv, which is used to read the csv file containing the data of the AC records.
"""

import pandas as pd

ebird_records_path = "./data_loading/data/ebird_data/crested_myna_records.csv"


class RecordsFromCsv():
    """
    read the csv file containing the data of the AC records.
    """

    def __init__(self, path_csv: str = ebird_records_path):
        """initialize the class"""
        self.path_csv = path_csv
        self.AC_data = self.read_csv()

    def read_csv(self):
        """
        This method is used to read the csv file.
        """
        AC_data = pd.read_csv(self.path_csv)
        AC_data = AC_data.astype(object)
        AC_data = self.convert_nan_to_none(AC_data)
        AC_data = self.fill_year_from_date(AC_data)
        AC_data = self.get_location_array(AC_data)
        return AC_data

    def convert_nan_to_none(self, in_df: pd.DataFrame):
        """
        This method is used to convert the nan values to none.
        """
        return in_df.where(pd.notnull(in_df), None)

    def fill_year_from_date(self, in_df: pd.DataFrame):
        """
        This method is used to fill the year from the observation_date.
        """
        in_df['observation_date'] = pd.to_datetime(in_df['observation_date'])
        in_df['year'] = in_df['observation_date'].dt.year
        return in_df

    def get_location_array(self, in_df: pd.DataFrame):
        """
        This method is used to get the location array from the dataframe.
        """
        in_df['location'] = in_df.apply(
            lambda row: [row['latitude'], row['longitude']], axis=1)
        return in_df

    def get_rows_list(self):
        """
        This method is used to get the rows list from the csv file.
        """
        self.AC_data = self.AC_data.to_dict(orient='index')
        AC_data_rows = [v for k, v in self.AC_data.items()]
        return AC_data_rows
