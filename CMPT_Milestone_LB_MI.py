
import load_route_data, load_shape_data

def main():
    '''
    purpose
    parameters
    return
    '''
    route_file_path = 'data/routes.txt'
    shapes_file_path = 'data/shapes.txt'
    trips_file_path = 'data/shapes.txt'
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
            route_names = load_route_names(filename)
            continue
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