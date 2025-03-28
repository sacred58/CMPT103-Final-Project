#------------------------------------
# Max Ingram, Liam Barnes
# Programming Project - Milestone#1
#------------------------------------

import pickle
from datetime import date
from graphics import *

def load_route_names(filename):
    '''
    purpose: Loads route ids and associated names into a dictionary
    parameters
        filename (str): filename of the route and names file
    return
        route_data (dictionary): dictionary with {route_id : route_name}
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
        route_name = routes[route]["name"].strip('"')
        print(f'Shape ids for route [{route_name}]')
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
    '''
    purpose: Get the shape with the longest list of coordinates attached to it
    parameters:
        routes (dict): the routes dictionary gotten above 
        shapes (str): dictionary of shape IDs and cordinates
    returns:
        None
    '''
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

def save_data(routes,shapes,disruptions,pickle_file_path):
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
            pickle.dump((routes, shapes, disruptions), file)
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
            routes, shapes, disruptions = pickle.load(file)
    except IOError as err:
        print(err)
        return
    return routes, shapes, disruptions

def load_disruptions(filename):
    '''
    purpose: Loads dispruption data from a CSV file for traffic disruptions
    parameters:
        - filename: path of the disruption data file
    return:
        - disruptions (date_reference, (lat, lon)): Set of tuples containing a reference to a date object and a nested tuple
        with the lat and lon of the disruption
    '''

    months = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    
    try:
        with open(filename, 'r') as file:
            file_lines = file.readlines()
            print(f'Data from {filename} loaded')
    except IOError as err:
        print(err)
        return
    
    disruptions = set()
    
    for lines in range(1, len(file_lines)):
        current_line = file_lines[lines].split(',')

        # Process date data
        # Turn the month into an int
        month_str, day = current_line[5].lower().split(' ')
        month_str = month_str[1:]

        if month_str in months.keys():
            month_int = months[month_str]

        day = int(day)

        year = int(current_line[6][:-1])

        d = date(year, month_int, day)

        # Process lon, lat data
        point = current_line[-1][7:-2]
        point = point.split(' ')

        point[0] = float(point[0])
        point[1] = float(point[1])
        point = tuple(point)

        disruptions.add((d, point))

    return disruptions

def lonlat_to_xy(win, lon, lat):
    '''Written by Philip Mees for CMPT 103
    Purpose: convert longitude/latitude locations to x/y pixel locations
        This avoids the use of the setCoords, toWorld, and toScreen methods and graphics.py incompatibilities
    Parameters:
        win (GraphWin): the GraphWin object of the GUI
        lon, lat (float): longitude and latitude to be converted
    Returns: x, y (int): pixel location inside win'''

    xlow, xhigh = -113.720049, -113.320418
    ylow, yhigh = 53.657116, 53.393703

    width, height = win.getWidth(), win.getHeight()

    x = (lon - xlow) / (xhigh - xlow) * width
    y = (lat - ylow) / (yhigh - ylow) * height

    return int(x), int(y)

def draw_disruptions(win, disruptions):
    '''
    purpose: Determine if a traffic disruption is still active and draw disruptions on map 
    accordingly
    parameters:
        - win: reference to window object containing the map
        - disruptions (set): set of traffic disruptions with date and lon and lat
    return:
        - None
    '''

    today = date.today()

    for element in disruptions:
        enddate, lonlat = element
        lon, lat = lonlat
        # If the traffic disruption is still ongoing
        if enddate > today:
            # Plot disruption on map
            x, y = lonlat_to_xy(win, lon, lat)
            disruption = Circle(Point(x, y), 5) 
            disruption.setFill('red')
            disruption.draw(win)
        else:
            continue

def draw_shape_id(win, shapes, shape_id):
    '''
    purpose
    parameters
    return
    '''

    coords = shapes[shape_id]

    for index in range(0, 2, len(coords)):
        lon, lat = coords[index]
        x1, y1 = lonlat_to_xy(win, lon, lat)
        start = Point()
        end = Point(coords[index + 1])
        line = Line(start, end)
        line.draw(win)
        
        






        
def graphical_interface(routes, route_names, shapes, disruptions):
    '''
    purpose: Define window with map and call coresponding helper functions for all functionality
    parameters: 
        - routes (dictionary): dictionary with route_id, route_name, and associated shape_ids
        - route_names (dictionary): dictionary with {route_id: route_name}
        - shapes (dictionary): dictionary with shape_ids and coordinates
        - disruptions (set): set with traffic disruptions locations and dates they are active
    return
        - None
    '''

    # Create basic window
    win = GraphWin('ETS Data', 800, 920)
    bkground = Image(Point(win.getWidth() // 2, win.getHeight() // 2), 'edmonton.png')
    bkground.draw(win)

    # Draw disruptions
    draw_disruptions(win, disruptions)

    # Search for routes
    # Draw according to shape_id
    draw_shape_id(win, shapes, '056-148-East')



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
    disruptions_file_path = 'data/traffic_disruptions.txt'
    route_names = None
    routes = None
    shapes = None
    disruptions = None

    options = '''
Edmonton Transit System
-------------------------
(1) Load route data
(2) Load shapes data
(3) Load disruptions data

(4) Print shape IDs for a route
(5) Print coordinates for a shape ID
(6) Find longest shape for route

(7) Save routes and shapes in a pickle
(8) Load routes and shapes from a pickle

(9) Interactive map
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
            filename = input('Enter a filename:').strip()

            if filename == '':
                filename = disruptions_file_path

            disruptions = load_disruptions(filename)
            
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
            if routes == None:
                print("Route data hasn't been loaded yet")
            elif shapes == None:
                print("Shape ID data hasn't been loaded yet")
            else:
                longest_shape(routes,shapes)
        elif user_input == '7':
            # Save route_names, routes, shapes in a pickle
            filename = input("Enter a filename: ")
            if filename == '':
                filename = pickle_file_path
            save_data(routes,shapes,disruptions,filename)
            print(f"Data structures successfully written to {filename}")
            continue
        elif user_input == '8':
            # Load route_names, routes, shapes from the aforementioned pickle
            filename = input("Enter a filename: ")
            if filename == '':
                filename = pickle_file_path
            try:
                routes, shapes,disruptions = load_data(filename)
            except:
                continue

            print(f'Data from {filename} loaded')
            
            continue
        elif user_input == '9':
            # Start graphical interface
            if routes == None or shapes == None or disruptions == None:
                print('ETS transit information not loaded yet')
            else:
                graphical_interface(routes, route_file_path, shapes, disruptions)
        elif user_input == '0':
            break

        else:
            print('Invalid Option')
            continue

main()
