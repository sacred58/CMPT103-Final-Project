
def get_shapeid(routes):
    '''
    
    '''
    route = input("Enter route: ").strip()
    if route in routes:
        print(f"Shape ids for route {routes[route]['name']}")
        for item in routes[route]['shape_ids']:
            print('\t' + str(item))
