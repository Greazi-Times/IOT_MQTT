import csv
import Computer.computer_constants as constants
from os.path import exists

#----------------------------------------------------------------------------------#
# Public values
#----------------------------------------------------------------------------------#

# name and place of the csv file
filename = str(constants.file)
# Boolean to see if the file has been loaded
setup = False
# field names
fields = ['Datum', 'Temp', 'Lucht Vochtigheid', 'Klep Stand']

#----------------------------------------------------------------------------------#
# Main systems
#----------------------------------------------------------------------------------#

# Create the startup method for the logging system
class startup:
    # Check if log file exists if not make one
    if (not exists(filename)):
        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # writing headers (field names)
            writer.writeheader()

def add(data):
    # writing to csv file
    with open(filename, 'a') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writerow(data)

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]