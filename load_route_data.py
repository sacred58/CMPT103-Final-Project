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

def load_routes(filename):