from menus.abstract_menu import AbstractMenu
from menus.route_menu import RouteMenu
from menus.stop_menu import StopMenu
from menus.directions_menu import DirectionsMenu
from views.stop_view import StopView
from views.route_view import RouteView
from views.directions_view import DirectionsView

class MainMenu(AbstractMenu):
    '''
    A CLI Menu meant to be a directory to sub menus.
    '''

    def __init__(self, route_view:RouteView, stop_view: StopView, directions_view: DirectionsView):
        self.route_view = route_view
        self.stop_view = stop_view
        self.directions_view = directions_view
    def printHelp(self):
        print('''
format: <command>: <description>
--------------------------------------
help: prints available commands
routes: opens route menu
stops: opens stops menu
directions: open route finding menu
exit: exit program
        ''')

    def end(self):
        pass

    def activate(self):
        command = ''
        command_options = {
            'routes':RouteMenu(self.route_view).activate
            ,'stops':StopMenu(self.route_view, self.stop_view).activate
            ,'directions':DirectionsMenu(self.route_view, self.stop_view, self.directions_view).activate

        }
        self.startCommandLoop('MAIN MENU', command_options)