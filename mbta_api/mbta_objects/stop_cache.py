from mbta_requests.stop_request import StopRequest
from mbta_requests.stop_options import StopOptions
from mbta_objects.stop import Stop
from mbta_objects.route_cache import RouteCache


class StopCache():
    """
    An object for holding, updating and manipulating the stop objects in memory.
    """


    def __init__(self):
        self.stops = {}


    def insertStop(self, stop:Stop):
        '''
        Stops can have several routes, so they may be duplicated, if stops are ingested per route.
        This method is used to upsert the stop in the StopCache. The only data that would be needed
        from a duplicated stop would be the additional route that contains the stop, so that is added.
        '''
        try:
            old_stop = self.stops[stop.id]
            old_stop.routes.extend(stop.routes)
        except KeyError:
            self.stops[stop.id] = stop


    def updateCacheForRoutes(self, route_cache:RouteCache, stop_request_options:StopOptions):
        """
        Fetches stops for each of the routes in the passed route cache and updates the StopCache.
        """

        for key in route_cache.routes:
            stop_request_options.filter_route = key
            stop_request_options.include = (stop_request_options.include or '') + ',route'
            stop_req = StopRequest(stop_request_options)
            new_stops = stop_req.getAll()
            for stop_key, stop in new_stops.items():
                self.insertStop(stop)


    def findJunctions(self) -> dict:
        """
        Returns a list of stops that have more than one route.
        """

        junctions = {}
        for stop_key, stop in self.stops.items():
            if len(stop.routes) > 1:
                junctions[stop_key] = stop
        return junctions


    