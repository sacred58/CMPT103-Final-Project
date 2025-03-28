
def longest_shape(routes,shapes):
    '''
    purpose: Get the shape with the longest list of coordinates attached to it
    parameters:
        routes (dict): the routes dictionary gotten above 
        shapes (str): dictionary of shape IDs and cordinates
    returns:
        None
    '''
    routeid = input("Enter route ID: ").strip()
    shapeids = []
    lengths = {}
    if routeid in routes:
        for item in routes[routeid]['shape_ids']:
            shapeids.append(item)
        for shape in shapes:
            lengths.update({shape:len(shapes[shape]['shape_id'])})
    else:
        print('\t' + "** NOT FOUND **")
    longest_shape = max(lengths, key=lengths.get)

    print(f"The longest shape for {routeid} is {longest_shape} with {len(lengths[longest_shape])} coordinates")
    
