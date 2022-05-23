from views.route_view import RouteView
from views.stop_view import StopView
from views.directions_view import DirectionsView
from menus.main_menu import MainMenu
from mbta_objects.stop_cache import StopCache
from mbta_objects.route_cache import RouteCache
from mbta_requests.stop_options import StopOptions
from mbta_requests.route_options import RouteOptions

route_cache = RouteCache()
stop_cache = StopCache()

if __name__ == '__main__':
    print('Updating Cache')

    # I chose to filter the contained caches with only routes of type 0 and 1, since that is what the prompt requested.
    # There is no need to hammer the MBTA's API, for unnecessary info and it would be trivial to change in the future, this way. 
    route_cache.updateCache(RouteOptions(filter_type='0,1'))
    stop_cache.updateCacheForRoutes(route_cache, StopOptions(include='child_stops,connecting_stops'))
    route_cache.updateRouteStops(stop_cache)
    route_cache.updateRouteConnections(stop_cache)
    route_view = RouteView(route_cache)
    stop_view = StopView(stop_cache)
    directions_view = DirectionsView(route_cache)
    MainMenu(route_view, stop_view, directions_view).activate()
