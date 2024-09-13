"""
This module contains the class RecordsFromCsv, which is used to read the csv file containing the data of the AC records.
"""

import pandas as pd


class RecordsFromCsv():
    """
    read the csv file containing the data of the AC records.
    """

    def __init__(self):
        """initialize the class"""
        self.path_csv = "./data_analysis/data/AC_american_records_csv.csv"

    def get_rows_list(self):
        """
        This method is used to get the rows list from the csv file.
        """
        AC_data = pd.read_csv(self.path_csv).to_dict(orient='index')
        AC_data_rows = [v for k,v in AC_data.items()]
        return AC_data_rows
