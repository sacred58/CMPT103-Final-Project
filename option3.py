# Creating menu option 3
from datetime import date # Date will need to be added at beginning of milestone2

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

        # Process lat, lon data
        point = current_line[-1][7:-2]
        point = point.split(' ')

        point[0] = float(point[0])
        point[1] = float(point[1])
        point = tuple(point)

        disruptions.add((d, point))

    return disruptions

print(load_disruptions('data/traffic_disruptions.txt'))

