def load_route_names(filename):
    try:
        with open(filename, 'r') as file:
            route = file.readlines()
    except IOError as err:
        print(err)
    route_data = {}
    for rows in range(1,len(route)):
        column = route[rows].split(',')
        route_data.update({column[0]:column[3]})
    return route_data

def load_routes(filename, route_names):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError as err:
        print(err)
    routes = {}
    for line in range(1, len(lines)):
        current_line = lines[line].split(',')
        routes[current_line[0]] = {'name':'', 'shape_ids': set()}

    for line in range(1, len(lines)):
        current_line = lines[line].split(',')
        routes[current_line[0]]['shape_ids'].add(current_line[6])

        # Printing for debug purposes
    
    for key in route_names:
        routes[key]['name'] = route_names[key]

    for key in routes:
        print(key, routes[key])
route_names = load_route_names('data/routes.txt')
load_routes('data/trips.txt', route_names)
        


