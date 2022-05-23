from menus.abstract_menu import AbstractMenu
from views.route_view import RouteView
from views.stop_view import StopView


class StopMenu(AbstractMenu):
    '''
    A CLI Menu meant interacting with the Stop View.
    '''

    def __init__(self, route_view:RouteView, stop_view: StopView):
        self.route_view = route_view
        self.stop_view = stop_view

    def printHelp(self):
        print('''
format: <command>: <description>
--------------------------------------
help: prints available commands
show_stops: Shows available stops
show_junctions: Shows all stops where multiple routes overlap.
exit: exit menu
        ''')

    def end(self):
        pass

    def activate(self):
        command_options = {
            'show_stops':self.stop_view.showStops
            ,'show_junctions':self.stop_view.showJunctions

        }
        self.startCommandLoop('STOP MENU', command_options)
