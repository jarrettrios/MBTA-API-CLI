from menus.abstract_menu import AbstractMenu
from views.route_view import RouteView
from views.stop_view import StopView
from views.directions_view import DirectionsView


class DirectionsMenu(AbstractMenu):
    '''
    A controller meant for interfacing with the directions view. Allows for the user to get directions from one stop to the other.
    '''

    def __init__(self, route_view:RouteView, stop_view: StopView, directions_view: DirectionsView):
        self.route_view = route_view
        self.stop_view = stop_view
        self.directions_view = directions_view
        self.beg_stop = None
        self.end_stop = None


    def printHelp(self):
        print('''
format: <command>: <description>
--------------------------------------
help: prints available commands
set_begin: Set your starting stop.
set_end: Set your destination stop.
show_selected: Show selected stops.
get_directions: Display which routes to take to get from one stop to another.
exit: exit menu
        ''')

    def end(self):
        pass
    
    def showSelectedStops(self):
        '''
        Prints the stops selected by the user.
        '''

        print()
        print(f'Start: {self.beg_stop.name} | End: {self.end_stop.name}')

    def chooseStart(self,):
        '''
        Navigates the users through selecting a stop, and assigns it to the starting location.
        '''

        print(f'Select Route that contains your starting stop.')
        self.beg_stop = self.chooseStop()  
            
    def chooseEnd(self):
        '''
        Navigates the users through selecting a stop, and assigns it to the destination.
        '''

        print(f'Select Route that contains your ending stop.')
        self.end_stop = self.chooseStop()

    def chooseStop(self):
        '''
        A method that takes user input to select a stop. 
        '''

        self.route_view.showRoutes()
        print()
        route = None
        # Loop to choose route by id. This filters the stops by routes, allowing for easier selection.
        while route is None:
            route = self.route_view.findRoute(input('Enter route-id. (case sensitive):'))
            if route is None:
                print('Unknown ID. Please try again.')

        print(f'Select Stop.')
        if route:
            for stop_id in route.stops:
                stop = self.stop_view.findStop(stop_id)
                print(f'{stop_id}: {stop.name}')
            print()
            stop = None
            while stop is None:
                stop = self.stop_view.findStop(input('Enter stop-id. (case sensitive):'))
                if stop is None:
                    print('Unknown ID. Please try again.')

            return stop

    def findDirections(self):
        '''
        A method that finds, then prints the path of routes that the user should take to make the trip from the starting location
        to the destination.
        '''

        print(f'To go from {self.beg_stop.name} to {self.end_stop.name} take the following routes:')
        self.directions_view.showRouteBetweenStops(self.beg_stop, self.end_stop)

    def activate(self):
        command_options = {
            'set_begin': self.chooseStart
            ,'set_end': self.chooseEnd
            ,'show_selected': self.showSelectedStops
            ,'get_directions': self.findDirections

        }
        self.startCommandLoop(f'DIRECTIONS MENU', command_options)