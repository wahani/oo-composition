import sys
import syslog
import pandas as pd

# The initial class.
# Super-Klasse mit
#  1. Property (DataFrame)
#  2. private Methode zum lesen der Daten
#  3. summary-Methode -- öffentliche Methode die den DataFrame analysiert (mean
#     )of cols
#  4. summary1-Methode -- verwendet summary Methode (mean of cols + round(0))

# Sub-Klasse
#  1. Braucht die Property
#  2. private_methode zum Lesen der Daten (überschreibt die method der super)
#  3. Eigene summary-Methode -- merge zwischen super-property und eigenem
#     Datensatz (eigener Datensatz enthält str)

# Wie sieht das Szenario aus wenn man es mit Composition macht?

#   - 1. Stubs von allen Methoden die wir brauchen, mit leerer Rückgabe
#   - 2. Tests für die Methoden
#   - 3. Implementieren der Methoden


class DataProvider():
    def __init__(self):

    def _read_data(self):
        return pd.DataFrame(data={
            'col1': [1.5, 2.8],
            'col2': [3.2, 4.1]})

    def summarize(self):
        self._read_data()
        # calculate mean


class SubClass(Provider):
    def __init__(self):
        self.sock = sock

    def _read_data(self):
        self.

    def summarize(self):
        self.log()
