# Sub-Klasse
#  1. Braucht die Property
#  2. private_methode zum Lesen der Daten (überschreibt die method der super)
#  3. Eigene summary-Methode -- merge zwischen super-property und eigenem
#     Datensatz (eigener Datensatz enthält str)

import pandas as pd
from composition.data_provider import DataProvider


class NewDataProvider(DataProvider):
    def __init__(self) -> None:
        self._new_provider_dataset = None

    @property
    def new_provider_dataset(self):
        return pd.DataFrame()

    def _read_data(self):
        return pd.DataFrame()

    def summarize(self):
        return pd.DataFrame()
