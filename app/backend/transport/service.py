import json


data =  json.load(open('data.json', 'r', encoding='utf-8'))

class TransportService:
    def __init__(self):
        self.data = data['transport']

    def get_all(self):
        return self.data
    
    def getComfortableOrEconomic(self, city: str):
        trip = list(filter(lambda x: x['city'] == city, self.data))
        
        mostEconomic = min(trip, key=self.__getByPrice)
        faster = min(trip, key=self.__getByTime)

        return {
            "mostEconomic": mostEconomic,
            "faster": faster
        }
    
    def avaliableCities(self):
        justCities = map(lambda x: x['city'], self.data)

        return list(set(justCities))
    

    def __getByTime(self, transport):
        return int(transport["duration"].removesuffix('h'))
    
    
    def __getByPrice(self, transport):
        return float(transport["price_econ"].removeprefix('R$ '))