from mbta_api.mbta_objects.route import Route
from mbta_api.mbta_objects.route_cache import RouteCache
from mbta_api.mbta_objects.stop import Stop
from mbta_api.mbta_objects.stop_cache import StopCache


test_stop = {
    'id': 'test id'
    ,'attributes': {
        'address': 'test address'
        ,'at_street': 'test at_street'
        ,'description': 'test description'
        ,'latitude': 'test latitude'
        ,'location_type': 'test location_type'
        ,'longitude': 'test longitude'
        ,'municipality': 'test municipality'
        ,'name': 'test name'
        ,'on_street': 'test on_street'
        ,'platform_code': 'test platform_code'
        ,'platform_name': 'test platform_name'
        ,'vehicle_type': 'test vehicle_type'
        ,'wheelchair_boarding': 'test wheelchair_boarding'
    }
    ,'relationships': {
        'route': {
            'data': {
                'id': 'test route'
            }
        }
        ,'child_stops': {
            'data': [
                {
                    'id': 'test child_stops'
                }
            ]   
        }
        ,'connecting_stops': {
            'data': [
                {
                    'id': 'test connecting_stops'
                }
            ]   
        }
        
    }
}

test_route = {
    'id': 'test id'
    ,'attributes': {
        'color': 'test color'
        ,'description': 'test description'
        ,'direction_destinations': 'test direction_destinations'
        ,'direction_names': 'test direction_names'
        ,'fare_class': 'test fare_class'
        ,'long_name': 'test long_name'
        ,'short_name': 'test short_name'
        ,'sort_order': 'test sort_order'
        ,'text_color': 'test text_color'
        ,'type': 'test type'
    }
}

test_routes_json = [
    {
    'id': 'red'
    ,'attributes': {
        'description': 'red route'
        ,'color': 'red'
        ,'direction_destinations': [0,1]
        ,'direction_names': ['west', 'east']
        ,'fare_class': 0
        ,'long_name': 'Red Line'
        ,'short_name': 'red'
        ,'sort_order': 0
        ,'text_color': '#000000'
        ,'type': 0
        }
    }, {
    'id': 'blue'
    ,'attributes': {
        'description': 'blue route'
        ,'color': 'blue'
        ,'direction_destinations': [0,1]
        ,'direction_names': ['north', 'south']
        ,'fare_class': 0
        ,'long_name': 'Blue Line'
        ,'short_name': 'blue'
        ,'sort_order': 1
        ,'text_color': '#000000'
        ,'type': 0
        }
    }, {
    'id': 'brown'
    ,'attributes': {
        'description': 'brown route'
        ,'color': 'brown'
        ,'direction_destinations': [0,1]
        ,'direction_names': ['north', 'south']
        ,'fare_class': 0
        ,'long_name': 'Brown Line'
        ,'short_name': 'brown'
        ,'sort_order': 2
        ,'text_color': '#000000'
        ,'type': 0
        }
    }, {
    'id': 'grey'
    ,'attributes': {
        'description': 'grey route'
        ,'color': 'grey'
        ,'direction_destinations': [0,1]
        ,'direction_names': ['west', 'east']
        ,'fare_class': 0
        ,'long_name': 'Grey Line'
        ,'short_name': 'grey'
        ,'sort_order': 3
        ,'text_color': '#000000'
        ,'type': 0
        }
    }
]

test_stops_json = [
    {
        'id': 'red-0'
        ,'attributes': {
            'name': 'Red Start'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'red'
                }
            }
            
        }
    }, {
        'id': 'red-blue'
        ,'attributes': {
            'name': 'Red Blue Junction'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'red'
                }
            }
            
        }
    }, {
        'id': 'red-blue'
        ,'attributes': {
            'name': 'Red Blue Junction'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'blue'
                }
            }
            
        }
    }, {
        'id': 'blue-0'
        ,'attributes': {
            'name': 'Blue middle'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'blue'
                }
            }
            
        }
    }, {
        'id': 'blue-grey'
        ,'attributes': {
            'name': 'Blue Grey Junction'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'blue'
                }
            }
        }
    }, {
        'id': 'blue-grey'
        ,'attributes': {
            'name': 'Blue Grey Junction'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'grey'
                }
            }
        }
    }, {
        'id': 'grey-brown'
        ,'attributes': {
            'name': 'Grey Brown Junction'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'grey'
                }
            }
        }
    }, {
        'id': 'grey-brown'
        ,'attributes': {
            'name': 'Grey Brown Junction'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'brown'
                }
            }
        }
    }, {
        'id': 'brown-0'
        ,'attributes': {
            'name': 'Brown Start'
        }
        ,'relationships': {
            'route': {
                'data': {
                    'id': 'brown'
                }
            }
        }
    }
    
]

test_routes_cache = RouteCache()
for route_json in test_routes_json:
    route = Route(route_json)
    test_routes_cache.routes[route.id] = route

test_stops_cache = StopCache()
for stop_json in test_stops_json:
    stop = Stop(stop_json)
    test_stops_cache.insertStop(stop)

test_routes_cache_completed = RouteCache()
for route_json in test_routes_json:
    route = Route(route_json)
    test_routes_cache_completed.routes[route.id] = route
test_routes_cache_completed.updateRouteConnections(test_stops_cache)
test_routes_cache_completed.updateRouteStops(test_stops_cache)

