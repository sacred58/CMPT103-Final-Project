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


route_names = load_route_names('data/routes.txt')
load_routes('data/trips.txt', route_names)
        


