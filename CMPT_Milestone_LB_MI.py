
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
    except IOError as err:
        print(err)
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
    '''
    #Check that the file exists
    try:
        with open(filename, 'r') as file:
            shape = file.readlines()
    except IOError as err:
        print(err)

    shapes = {}
    #create a dictionary with each of the shapeIDs, the empty list to fill in with lat/long after
    for rows in range(1,len(shape)):
        column = shape[rows].split(',')
        shapes.update({column[0]:[]})
    #fill in the lat/long list
    for rows in range(1,len(shape)):
        column = shape[rows].split(',')
        shapes[column[0]].append(f'{column[1]},{column[2]}')
    return shapes

def main():
    '''
    purpose
    parameters
    return
    '''
    route_file_path = 'data/routes.txt'
    shapes_file_path = 'data/shapes.txt'
    trips_file_path = 'data/trips.txt'
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

            if filename == '':
                filename = trips_file_path
            
            route_names = load_route_names(route_file_path)
            routes = load_routes(filename, route_names)
            print(f'data from {filename} loaded')

            for key in routes:
                print(f'{key} : {routes[key]}')
            # Call function to load data
        elif user_input == '2':
            #Prompt user for file name (With default set to the default path)
            continue
            # Call function to load data
        elif user_input == '3':
            print("Reserved for future use")
        elif user_input == '4':
            # Print shape ids for route from routes dictionary
            continue
        elif user_input == '5':
            # Prompt user for a shape id
            # find shape coordinates and print them
            continue
        elif user_input == '6':
            print('Reserved for future use')
        elif user_input == '7':
            # Save route_names, routes, shapes in a pickle
            continue
        elif user_input == '8':
            # Load route_names, routes, shapes from the aforementioned pickle
            continue
        elif user_input == '9':
            print('Reserved for future use')
        elif user_input == '0':
            break

        else:
            print('Invalid Option')
            continue

main()