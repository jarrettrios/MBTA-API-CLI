
from mbta_objects.route_cache import RouteCache

class DirectionsView():
    def __init__(self, route_cache:RouteCache):
        self.__route_cache = route_cache


    def showRouteBetweenStops(self, beg_stop, end_stop):
        '''
        This prints the results of findRouteBetweenShops, in order.
        '''

        path = self.__findRouteBetweenStops(beg_stop, end_stop)
        path_string = ''
        for route in path:
            path_string += f' ---> {route.long_name}'
        print(path_string.removeprefix(' ---> '))
        

    def __findRouteBetweenStops(self, beg_stop, end_stop):
        '''
        Takes two stop objects and returns a list that contains 
        the routes (in order) that link the two stops, using the mininum amount transfers.
        '''

        beg_routes = []
        end_routes = []
        for beg_route_key in beg_stop.routes:
            beg_routes.append(self.__route_cache.routes[beg_route_key])
        for end_route_key in end_stop.routes:
            end_routes.append(self.__route_cache.routes[end_route_key])

        min_transfer_path = []
        for beg_route in beg_routes:
            for end_route in end_routes:
                path_build_info = self.__bfs(beg_route, end_route)
                if path_build_info:
                    path = self.__buildPath(path_build_info[0], path_build_info[1], path_build_info[2])
                    path.reverse()
                    if len(min_transfer_path) == 0 or len(path):
                        min_transfer_path = path
        return min_transfer_path


    def __bfs(self, start, goal):
        '''
        An implementation of breadth-first-search, that returns the info needed to build the smallest path.
        '''

        queue = [start]
        explored = [start]
        parent_indices = [-1]
        while len(queue) > 0:
            vertex = queue.pop(0)
            current_index = explored.index(vertex)
            if vertex == goal:
                return (explored, parent_indices, current_index)
            for edge in vertex.connections:
                if edge not in explored:
                    explored.append(edge)
                    queue.append(edge)
                    parent_indices.append(current_index)
        return None


    def __buildPath(self, explored, parent_indices, goal_index) -> list:
        '''
        A method to build the path from __bfs back from the captured path-finding information.
        '''

        path = []
        while goal_index >= 0:
            path.append(explored[goal_index])
            goal_index = parent_indices[goal_index]
        return path