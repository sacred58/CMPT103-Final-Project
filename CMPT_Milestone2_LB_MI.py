#------------------------------------
# Max Ingram, Liam Barnes
# Programming Project - Milestone#1
#------------------------------------

import pickle

def load_route_names(filename):
    '''
    purpose: Loads route ids and associated names into a dictionary
    parameters
        filename (str): filename of the route and names file
    return
        route_data (str): dictionary with {route_id : route_name}
    '''

    # Catching file not found error
    try:
        with open(filename, 'r') as file:
            route = file.readlines()
    except IOError as err:
        print(err)
        return
    route_data = {}

    # For each line in the file, collects route id and route name
    for rows in range(1,len(route)):
        column = route[rows].split(',')
        route_data.update({column[0]:column[3]})
    return route_data

def load_routes(filename, route_names):
    '''
    purpose: Creates a dictionary with route ids, route names, and the shape_ids associated with the route
    parameters:
        - filename (str): filename to load the trips file with shape_ids
        - route_names: (dictionary): dictionary of route ids and route names in order to add them to the final output
    return
        - Dictionary with route_id, route name, and associated shape ids, setup like this:
        routes = {route_id:{name:route_name, shape_ids: {set of shape ids}}}
    '''

    # Check if route names have been loaded, required for this function
    if route_names == None:
        return

    # Catching file not found error
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f'Data from {filename} loaded')
    except IOError as err:
        print(err)
        return
    routes = {}

    # Collects all the route ids
    for line in range(1, len(lines)):
        current_line = lines[line].split(',')
        routes[current_line[0]] = {'name':'', 'shape_ids': set()}

    # Collects all the shape ids and adds them to the set of shape ids
    for line in range(1, len(lines)):
        current_line = lines[line].split(',')
        routes[current_line[0]]['shape_ids'].add(current_line[6])

    # adds names with data collected from load_route_names
    for key in route_names:
        routes[key]['name'] = route_names[key]
    
    return routes

def load_shapes(filename):  
    '''
    purpose: read through shape data and get the connected lat/long pairs
    parameters:
        filename (str): the file path to the shape data
    returns:
        shapes (dict): a dictionary containing a list of lat/long pairs connected to a shape ID
        shapes = {shape_id:[(lat,long),(lat,long)]}
    '''
    #Check that the file exists
    try:
        with open(filename, 'r') as file:
            shape = file.readlines()
            print(f'Data from {filename} loaded')
    except IOError as err:
        print(err)
        return

    shapes = {}
    #create a dictionary with each of the shapeIDs, the empty list to fill in with lat/long after
    for rows in range(1,len(shape)):
        column = shape[rows].split(',')
        shapes.update({column[0]:[]})
    #fill in the lat/long list
    for rows in range(1,len(shape)):
        column = shape[rows].split(',')
        shapes[column[0]].append((column[1],column[2]))  

    return shapes

def get_shapeid(routes):
    '''
    purpose: print all the shapeids connected to a route id
    parameters:
        routes (dict): the routes dictionary gotten above 
    return: None
    '''
    route = input("Enter route: ").strip()
    if route in routes:
        print(f"Shape ids for route [{routes[route]['name'].strip('"')}]")
        for item in routes[route]['shape_ids']:
            print('\t' + str(item))
    else:
        print('\t' + "** NOT FOUND **")


def search_shape_id(shapes, shape_id):
    '''
    purpose: Prints co-ordinates of a given shape id
    parameters:
        - shapes (str): dictionary of shape IDs and cordinates
        - shape_id (str): Shape ID to search for
    return:
        - None
    '''

    try:
        shape = shapes[shape_id]
    except KeyError:
        print("\t** NOT FOUND **")
        return
    
    print(f'Shape ID coordinates for {shape_id} are:')
    for coord in shape:
        print(coord)
    
def longest_shape(routes,shapes):
    routeid = input("Enter route ID: ")
    longest_shape = None
    highest = 0
    if routeid in routes:
        for shape in routes[routeid]['shape_ids']:
            if len(shapes[shape]) > highest:
                highest = len(shapes[shape])
                longest_shape = shape
    else:
        print('\t' + "** NOT FOUND **")

    print(f"The longest shape for {routeid} is {longest_shape} with {highest} coordinates")

def save_data(routes,shapes,pickle_file_path):
    '''
    purpose: saves pickled data to a file
    parameters:
        routes (dict): Dictionary with route_id, route name, and associated shape ids, setup like this:
        routes = {route_id:{name:route_name, shape_ids: {set of shape ids}}}

        shapes (dict): a dictionary containing a list of lat/long pairs connected to a shape ID, setup like this:
        shapes = {shape_id:[(lat,long),(lat,long)]}

        pickle_file_path (str): file to load from, defaults to data/etsdata.p
    return:
        None
    '''
    try:
        with open(pickle_file_path, 'wb') as file:
            pickle.dump((routes, shapes), file)
    except IOError as err:
        print(err)
        return

def load_data(pickle_file_path):
    '''
    purpose: loads pickled data from file
    parameters:
        pickle_file_path (str): file to load from, defaults to data/etsdata.p
    return:
        routes (dict): Dictionary with route_id, route name, and associated shape ids, setup like this:
        routes = {route_id:{name:route_name, shape_ids: {set of shape ids}}}

        shapes (dict): a dictionary containing a list of lat/long pairs connected to a shape ID, setup like this:
        shapes = {shape_id:[(lat,long),(lat,long)]}
    '''
    try:
        with open(pickle_file_path, 'rb') as file:
            routes, shapes = pickle.load(file)
    except IOError as err:
        print(err)
        return
    return routes, shapes
def main():
    '''
    purpose: Runs a menu to select other functions to load and view transit data
    parameters: None
    return: None
    '''
    route_file_path = 'data/routes.txt'
    shapes_file_path = 'data/shapes.txt'
    trips_file_path = 'data/trips.txt'
    pickle_file_path = 'data/etsdata.p'
    route_names = None
    routes = None
    shapes = None

    options = '''
Edmonton Transit System
-------------------------
(1) Load route data
(2) Load shapes data
(3) Reserved for future use

(4) Print shape IDs for a route
(5) Print coordinates for a shape ID
(6) Reserved for future use

(7) Save routes and shapes in a pickle
(8) Load routes and shapes from a pickle

(9) Reserved for future use
(0) Quit
'''

    while True:
        print(options)
        user_input = input("Enter Comand: ").strip()

        if user_input == '1':
            # Prompt user for file name (With default set to default path)
            filename = input("Enter a filename: ").strip()

            # If user does not enter anything, default to the default trips file path
            if filename == '':
                filename = trips_file_path
            
            route_names = load_route_names(route_file_path)
            routes = load_routes(filename, route_names)

        elif user_input == '2':
            #Prompt user for file name (With default set to the default path)
            filename = input("Enter a filename: ").strip()

            if filename == '':
                filename = shapes_file_path

            shapes = load_shapes(filename)
            
        elif user_input == '3':
            print("Option 3 reserved for Milestone#2")
        elif user_input == '4':
            # Print shape ids for route from routes dictionary
            if routes == None:
                print("Route data hasn't been loaded yet")
            else:
                get_shapeid(routes)
            continue
        elif user_input == '5':

            if shapes == None:
                print("Shape ID data hasn't been loaded yet")
            else:
                user_input = input("Enter shape ID: ").strip()
                search_shape_id(shapes, user_input)

 
            continue
        elif user_input == '6':
            longest_shape(routes,shapes)
        elif user_input == '7':
            # Save route_names, routes, shapes in a pickle
            filename = input("Enter a filename: ")
            if filename == '':
                filename = pickle_file_path
            save_data(routes,shapes,filename)
            print(f"Data structures successfully written to {filename}")
            continue
        elif user_input == '8':
            # Load route_names, routes, shapes from the aforementioned pickle
            filename = input("Enter a filename: ")
            if filename == '':
                filename = pickle_file_path
            try:
                routes, shapes = load_data(filename)
            except:
                continue

            print(f'Data from {filename} loaded')
            
            continue
        elif user_input == '9':
            print('Option 9 reserved for Milestone#2 ')
        elif user_input == '0':
            break

        else:
            print('Invalid Option')
            continue

main()