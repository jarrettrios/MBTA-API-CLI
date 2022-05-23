# MBTA-Routerfinder

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
 
------------------------------------------------------------------------

Question 1:

-To view all "subway" (Light and Heavy Rail Types) routes, navigate from the main menu to the routes menua by using the command "routes". Then enter the command "show_routes".


Question 2:
- To view the name of the subway route with the most stops as well as a count of its stops, navigate from the main menu to the routes menu by using the command "routes". Then enter the command "max_stops".

- To view the name of the subway route with the fewest stops as well as a count of its stops, navigate from the main menu to the routes menu by using the command "routes". Then enter the command "min_stops".

- To view A list of the stops that connect two or more subway routes along with the relevant route names for each of those stops, navigate from the main menu to the stops menu by using the command "stops". Then enter the command "show_junctions".

Question 3:
 
- To find a subway route between two stops, navigate from the main menu to the directions menu by using the command "directions". Then choose your beginning stop, by entering the command "set_begin". 
	- You will be shown a list of routes, choose your beginning route by entering its id, as shown in the list (the id is case sensitive). 
	- Next you will be shown all the stops for that route, choose your beginning stop by entering its id, as shown in the list (the id is case sensitive).
Then choose your destination stop, by entering the command "set_end".  
	- You will be shown a list of routes, choose your destination route by entering its id, as shown in the list (the id is case sensitive). 
	- Next you will be shown all the stops for that route, choose your destination stop by entering its id, as shown in the list (the id is case sensitive).
verify that you chose the correct stops by typing the command "show_selected" then type "get_directions" to get the series of routes you should take, to get from one stop to the other.



------------------------------------------------------------------------

For this assignment, I took inspiration from the MVC pattern. I considered the 'cache' objects to be the models, the "views" to be the views, and the menus to be the "controllers". This would allow for separation of UI and the underlying data model to allow for features to be more easily added.
To solve the patching problem, I made sure that the routes were a graph, and each route had a pointer to its connecting routes, which I was able to determine via the list of junctions. Then I started a breadth first search to search for the route with the least amount of transfers. BFS is an O(V + E) solution,
since in the worst case, the algorithm will visit each route (and its connecting vertice or pointer) in the graph. The algorithm searched for the first connected path it found for each starting route (if the beginning route was a junction) and for each ending route (if the ending stop was a junction), and returned the path with the least transfers between them. 
The program is currently set to only return a pre-filtered list of routes from the MBTA's api, to save from unnecessary calls to the API.