# MBTA-API-CLI

Requirements:
-Python
-pip
-Pipenv

Installing and running the program:

The following project contains two packages. The mbta_api package contains a cli for finding directions between two different stops of the MBTA. Follow the CLI's prompts for finding which routes to take, to get from your two selected stops.

The second package is the test package. if any changes to the existing code are made, run "python -m unittest disover" from the root of the project to run all tests. 

This project utilizes pipenv to manage its dependencies. If you wish to run the project, please install pipenv(https://pipenv.pypa.io/en/latest/) and then run 'pipenv install' in the main directory. 

After the dependencies are installed in the virtual enviroment, run "pipenv run python mbta_api/mbta_api_cli.py" from the project root, from your command line to launch the CLI.

TThe program will look to the enviromental variable MBTA_API_KEY for your API key.
 