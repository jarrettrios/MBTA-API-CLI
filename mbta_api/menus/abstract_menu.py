from abc import ABC, abstractmethod

class AbstractMenu(ABC):
    '''
    An Abstract class for making CLI Menus to act as a controller for this MBTA API CLI.
    '''

    @abstractmethod
    def printHelp(self):
        '''
        This method prints out the available commands for its menu.
        '''

        pass

    @abstractmethod
    def end(self):
        '''
        This method ends the current menu command loop. If any cleanup is needed, it is handled here.
        '''

        pass

    @abstractmethod
    def activate(self):
        '''
        This method starts creates the command loop option dictionary, and call "startCommandLoop" to start the menu.
        '''

        pass

    def startCommandLoop(self, menu_name, command_options):
        '''
        This starts the command loop with the given command_options (A dictionary that maps user-input -> method).
        '''

        command_options = {
            **command_options,             
            'help': self.printHelp
            ,'exit': self.end
        }
        self.printHelp()
        print('For a list of available commands, enter "help".')
        print('-----------------------------------------------')

        command = ''
        while command.lower() != 'exit':
            command = input(f'{menu_name} - Enter command:')
            print()
            try:
                command_options[command.lower()]()
            except KeyError:
                print('Unrecognized command, please try again. For a list of available commands, enter "help"')