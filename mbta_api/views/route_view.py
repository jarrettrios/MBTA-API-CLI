
from mbta_objects.route_cache import RouteCache

class RouteView():
    def __init__(self, route_cache:RouteCache):
        self.__route_cache = route_cache
    
    def showRoutes(self):
        print('Listing Cached Routes')
        print('<id>: <name>')   
        print('-----------------')
        for route_key, route in self.__route_cache.routes.items():
            print(f'{route_key}: {route.long_name}')

    def showRouteMaxStops(self):
        max_stops = self.__route_cache.routeWithMaxStops()
        print(f'Route with Most Stops: {max_stops.long_name} - {len(max_stops.stops)} Stops')

    def showRouteMinStops(self):
        min_stops = self.__route_cache.routeWithMinStops()
        print(f'Route with Least Stops: {min_stops.long_name} - {len(min_stops.stops)} Stops')

    def findRoute(self, route_id):
        """
        Returns the route that has the corresponding route_id, or None if no route was found.
        """

        try:
            return self.__route_cache.routes[route_id]
        except KeyError:
            return None