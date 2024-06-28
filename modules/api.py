import requests

class Manager:
    def __init__(self):
        self._api = API()

    def get_data(self):
        return self._api.get_data()
    