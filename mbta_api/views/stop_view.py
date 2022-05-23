
from mbta_objects.stop_cache import StopCache

class StopView():
    def __init__(self, stop_cache: StopCache):
        self.__stop_cache = stop_cache
    
    def showStops(self):
        print('Listing Cached Stops')
        print('<id>: <name>')   
        print('-----------------')
        for key, stop in self.__stop_cache.stops.items():
            print(f'{key}: {stop.name}')

    def showJunctions(self):
        print('Listing Junctions')
        print('<id>: <name>')   
        print('-----------------')
        junctions = self.__stop_cache.findJunctions()
        for key, junction in junctions.items():
            print(f'{key}: {junction.name} - {junction.routes}')


    def findStop(self, stop_id):
        '''
        returns the stop with the key of "stop_id". Returns None, if a stop wasn't found.
        '''
        try:
            return self.__stop_cache.stops[stop_id]
        except KeyError:
            return None