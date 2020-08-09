import csv

class Config:
    def __init__(self, csvName):
        self._name = csvName
        self._data = None
        self.load()
    
    def load(self):
        reader = csv.reader(open(self._name, 'r'))
        d = {}
        for row in reader:
            k, v = row
            d[k] = v
        self._data = d

    @property
    def data(self):
        return self._data

    @property
    def name(self):
        return self._name

    def getValue(self, key):
        return self._data[key]

    def setValue(self, key, value):
        self._data[key] = value


    