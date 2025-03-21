import pickle

filename = 'etsdata.p'
def save_data(routes,shapes):
    with open(filename, 'wb') as file:
        pickle.dump((routes, shapes), file)

def load_file():
    with open(filename, 'rb') as file:
        routes, shapes = pickle.load(file)