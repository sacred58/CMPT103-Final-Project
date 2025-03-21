
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
