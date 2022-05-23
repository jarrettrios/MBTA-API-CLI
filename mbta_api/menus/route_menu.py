from menus.abstract_menu import AbstractMenu
from views.route_view import RouteView


class RouteMenu(AbstractMenu):
    '''
    A CLI Menu meant interacting with the Route View.
    '''

    def __init__(self, route_view:RouteView):
        self.__route_view = route_view

    def printHelp(self):
        print('''
format: <command>: <description>
--------------------------------------
help: prints available commands
show_routes: Shows available routes
max_stops: Shows Route with the most stops.
min_stops: Shows Route with the least stops.
exit: exit menu
        ''')

    def end(self):
        pass

    def activate(self):
        command = ''
        command_options = {
            'show_routes':self.__route_view.showRoutes
            ,'max_stops':self.__route_view.showRouteMaxStops
            ,'min_stops':self.__route_view.showRouteMinStops

        }
        self.startCommandLoop('ROUTE MENU', command_options)