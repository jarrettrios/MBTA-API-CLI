class StopOptions():
        '''
        An object that represents all of the optional parameters for the MBTA API V3.0 Stop GET request

        --------------------------------

        Arguments:
        
        page[offset] -  Offset (0-based) of first element in the page.
        
        page[limit] - Max number of elements to return.
        
        sort - Results can be sorted by the id or any /data/{index}/attributes key. Assumes ascending; may be prefixed with '-' for descending
        
        fields[route] - Fields to include with the response. Multiple fields MUST be a comma-separated (U+002C COMMA, “,”) list.
        
        include - Relationships to include (eg. stop/line/route_patterns). "stop" can only be included when filter[stop] is also specified. Multiple fields MUST be a comma-separated (U+002C COMMA, “,”) list.
        
        filter[stop] - Filter by id. Multiple IDs MUST be a comma-separated (U+002C COMMA, “,”) list.
        
        filter[type] - 0: Light Rail, 1: Heavy Rail, 2: Commuter Rail, 3: Bus, 4: Ferry. | Multiple route_type MUST be a comma-separated (U+002C COMMA, “,”) list.
        
        filter[direction_id] - Filter by direction of travel along the route. Must be used in conjuction with filter[route] to apply.

        filter[date] - Filter by date that route is active The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD.

        filter[id] - Filter by multiple IDs. Multiple IDs MUST be a comma-separated (U+002C COMMA, “,”) list.

        '''
        def __init__(self, page_offset:int = None, page_limit:int = None, sort:str = None, 
        fields_stop:str = None, include:str = None, filter_latitude:str = None, filter_longitude:str = None, 
        filter_direction_id:str = None, filter_date:str = None, filter_radius:int = None, filter_id:str = None, 
        filter_route_type:str = None, filter_route:str = None, filter_service:str = None, filter_location_type:str = None
        ):
            self.page_offset = page_offset
            self.page_limit = page_limit
            self.sort = sort
            self.fields_stop = fields_stop
            self.include = include
            self.filter_date = filter_date
            self.filter_direction_id = filter_direction_id
            self.filter_latitude = filter_latitude
            self.filter_longitude = filter_longitude
            self.filter_radius = filter_radius
            self.filter_id = filter_id
            self.filter_route_type = filter_route_type
            self.filter_route = filter_route
            self.filter_service = filter_service
            self.filter_location_type = filter_location_type
