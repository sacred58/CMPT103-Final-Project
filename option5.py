from CMPT_Milestone_LB_MI import load_shapes

def search_shape_id(shapes, shape_id):

    try:
        shape = shapes[shape_id]
    except:
        print("\t** NOT FOUND **")
        return
    
    print(f'Shape ID coordinates for {shape_id} are:')
    for coord in shape:
        print(coord)

shapes = load_shapes('data/shapes.txt')
search_shape_id(shapes, '112-3-East')