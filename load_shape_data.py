filename = 'data/shapes.txt'
def load_shapes(filename):  
    try:
        with open(filename, 'r') as file:
            shape = file.readlines()
    except IOError as err:
        print(err)
    shapes = {}
    for rows in range(1,len(shape)):
        column = shape[rows].split(',')
        shapes.update({column[0]:[]})
    for rows in range(1,len(shape)):
        column = shape[rows].split(',')
        shapes[column[0]].append(f'{column[1]},{column[2]}')
    return shapes
