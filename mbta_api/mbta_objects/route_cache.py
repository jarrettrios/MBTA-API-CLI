from mbta_requests.route_options import RouteOptions
from mbta_requests.route_request import RouteRequest
from mbta_objects.route import Route


class RouteCache():
    """
    An object for holding, updating and manipulating the route objects in memory.
    """
    def __init__(self):
        self.routes = {}

    def updateCache(self, routeRequestOptions:RouteOptions):
        """
        Get alls routes returned with a GET request and the passed parameters
        """

        route_req = RouteRequest(routeRequestOptions)
        self.routes = route_req.getAll()

    def updateRouteStops(self, stop_cache):
        """
        Add child stops to routes contained in the cache, from the passed StopCache
        """

        for stop_key, stop in stop_cache.stops.items():
            for route_key in stop.routes:
                route = self.routes[route_key]
                route.stops[stop_key] = stop

    def updateRouteConnections(self, stop_cache):
        """
        Uses child stops to make an unweighted graph of all the routes contained in the cache.
        """

        for junction_key, junction in stop_cache.findJunctions().items():
            for route_key in junction.routes:
                route = self.routes[route_key]
                for connection_key in junction.routes:
                    connection = self.routes[connection_key]
                    if connection_key != route_key and connection != route:
                        route.connections.append(connection)


    def routeWithMaxStops(self) -> Route:
        """
        Returns the route with the most stops.
        """

        current_max = None
        for route_key, route in self.routes.items():
            if (current_max is None) or (len(route.stops) > len(current_max.stops)):
                current_max = route
        return current_max

    def routeWithMinStops(self) -> Route:
        """
        Returns the route with the least stops.
        """

        current_min = None
        for route_key, route in self.routes.items():
            if (current_min is None) or (len(route.stops) < len(current_min.stops)):
                current_min = route
        return current_min
    