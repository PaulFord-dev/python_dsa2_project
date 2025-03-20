# Module that handles functions related to distance
import csv

# Inputs distances from CSV into a 2D list and returns the list
def load_distances(file: csv) -> list:
    distance_data_list = []
    with open(file) as csv_data:
        distance_data = csv.reader(csv_data, delimiter=',')
        for row in distance_data:
            distance_data_list.append(row)
    return distance_data_list

# Inputs addresses from CSV file into a list and returns the list
def load_addresses(file: csv) -> list:
    address_data_list = []
    with open(file) as csv_data:
        address_data = csv.reader(csv_data, delimiter=',')
        for row in address_data:
            address_data_list.append(row[2])
    return address_data_list

# Finds the distance between two addresses and returns the mileage as a float
# Used in the delivery
def get_distances(address1: str, address2: str, address_list: list, distance_list: list) -> float:
    distance = 0.0
    index1 = address_list.index(address1)
    index2 = address_list.index(address2)
    distance = distance_list[index1][index2]
    if len(distance) == 0:
        distance = distance_list[index2][index1]
    return distance


