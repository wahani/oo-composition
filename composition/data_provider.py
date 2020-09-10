# The initial class.
# Super-Klasse mit
#  1. Property (DataFrame)
#  2. private Methode zum lesen der Daten
#  3. summary-Methode -- öffentliche Methode die den DataFrame analysiert (mean
#     )of cols
#  4. summary1-Methode -- verwendet summary Methode (mean of cols + round(0))


# Wie sieht das Szenario aus wenn man es mit Composition macht?

#   - 1. Stubs von allen Methoden die wir brauchen, mit leerer Rückgabe
#   - 2. Tests für die Methoden
#   - 3. Implementieren der Methoden

import pandas as pd


class DataProvider():
    def __init__(self) -> None:
        self._provider_dataset = None

    @property
    def provider_dataset(self):
        return pd.DataFrame()

    def _read_data(self):
        return pd.DataFrame()

    def summarize(self):
        return pd.DataFrame()

    def summarize_rounded(self):
        return pd.DataFrame()


data = {
    'col1': [1.5, 2.8],
    'col2': [3.2, 4.1]}
