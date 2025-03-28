import CMPT_Milestone2_LB_MI
CMPT_Milestone2_LB_MI.main()
def longest_shape(routes,shapes):
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
    
#{route_id:{name:route_name, shape_ids: {set of shape ids}}}
#{shape_id:[(lat,long),(lat,long)]}