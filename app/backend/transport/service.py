import json


data =  json.load(open('data.json', 'r'))

class TransportService:
    def __init__(self):
        self.data = data['transport']

    def get_all(self):
        return self.data
    