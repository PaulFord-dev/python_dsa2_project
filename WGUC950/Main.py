# Paul Ford  Student ID: 001538238

# Main module of program.  Creates objects and uses methods and functions to fulfill program requirements.
from datetime import datetime

import Distance
import Loading
import tkinter

from HashMap import HashMap
from Truck import Truck

# Creates HashMap object
package_hash_map = HashMap()

# Takes package data from CSV file and creates Package objects and inputs them into HashMap object
Loading.load_package("packageCSV.csv", package_hash_map)

# Takes distance data from CSV file and inputs into 2D list
distance_data_list = Distance.load_distances("distanceCSV.csv")

# Takes address data from CSV file and inputs into a list
address_data_list = Distance.load_addresses("addressCSV.csv")

# Corrects address
package_9 = package_hash_map.find_package(9)
package_9.address = '410 S State St'

# This block creates three truck objects and three lists which contain the keys for each package to be loaded onto each truck
# The lists are updated as the delivery function iterates through each truck object
truck1_list = [1, 13, 14, 5, 15, 16, 19, 20, 29, 30, 31, 37, 40]
truck1 = Truck(1)
truck2_list = [2, 3, 4, 7, 8, 18, 6, 25, 32, 34, 28, 36, 38]
truck2 = Truck(2)
truck2.update_time(65)
truck3_list = [9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]
truck3 = Truck(3)

# The total number of packages to be delivered
number_of_packages = len(truck1_list) + len(truck2_list) + len(truck3_list)

# Loads package list into first two truck objects
# Updates package status to "En Route" and gives packages a Truck ID
Loading.load_packages_to_truck(truck1, truck1_list, package_hash_map)
Loading.load_packages_to_truck(truck2, truck2_list, package_hash_map)

# Runs delivery algorithm for first two truck objects
# Iterates through truck list and finds next closest package and updates truck and package status and time accordingly
truck1.deliver_packages(address_data_list, distance_data_list, package_hash_map)
truck2.deliver_packages(address_data_list, distance_data_list, package_hash_map)

# This code block sets truck 3 start time
# It will set the time of truck 3 to the first truck to return
# Also holds truck time to 10:20 for a delayed package
if truck1.time < truck2.time:
    truck3.time = truck1.time
else:
    truck3.time = truck2.time
if truck3.time < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 10, 20, 0, 0):
    truck3.time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 10, 20, 0, 0)

# With a start time the third truck now loads and delivers just as the other trucks above
# Loads package list into third truck object
Loading.load_packages_to_truck(truck3, truck3_list, package_hash_map)

# Runs delivery algorithm for third truck object
truck3.deliver_packages(address_data_list, distance_data_list, package_hash_map)

# Total mileage for delivering all packages
total_mileage = truck1.mileage + truck2.mileage + truck3.mileage

# Requirement B
# A look-up function that takes in package ID and returns all package info
def return_all_package_variables(ID):
    package = package_hash_map.find_package(ID)
    address = package.address
    deadline = package.deadline
    city = package.city
    zipcode = package.zipcode
    weight = package.weight
    status = package.status
    delivery_time = package.delivery_time

    return address, deadline, city, zipcode, weight, status, delivery_time

# Checks all packages were delivered before deadline
def check_arrival_time(hashmap):
    ontime_delivery = True
    for j in range(1, number_of_packages + 1):
        package = hashmap.find_package(j)
        package_deadline = package.parse_deadline()
        if package.delivery_time > package_deadline:
            print(f'Package {package.ID} did not meet delivery deadline')
            ontime_delivery = False
    if ontime_delivery:
        print(f'All packages met delivery deadline')
    return

check_arrival_time(package_hash_map)

# Prints package status of all packages at a given time
# Is called to display information requested by user via user interface
def delivery_status_from_time(input_time, hashmap) -> None:

    for j in range(1, number_of_packages + 1):
        package = hashmap.find_package(j)
        if input_time < package.time_loaded:
            if package.ID == 9:
                package.address = '300 State St'
            print(f'Package ID: {package.ID} | '
                  f'Destination: {package.address} {package.city} {package.state} {package.zipcode} | '
                  f'Deadline: {package.deadline} | '
                  f'Weight: {package.weight} kilograms | '
                  f'Truck: {package.truck} | '
                  f'Status: At Hub\n')
            if package.ID == 9:
                package.address = '410 S State St'
        elif input_time > package.time_loaded and input_time < package.delivery_time:
            print(f'Package ID: {package.ID} | '
                  f'Destination: {package.address} {package.city} {package.state} {package.zipcode} | '
                  f'Deadline: {package.deadline} | '
                  f'Weight: {package.weight} kilograms | '
                  f'Truck: {package.truck} | '
                  f'Status: In Transit\n')
        elif input_time > package.delivery_time:
            print(f'Package ID: {package.ID} | '
                  f'Destination: {package.address} {package.city} {package.state} {package.zipcode} | '
                  f'Deadline: {package.deadline} | '
                  f'Weight: {package.weight} kilograms | '
                  f'Truck: {package.truck} | '
                  f'Status: Delivered at {package.delivery_time}\n')
    return

# Returns package status of a particular package at a given time
# Is called to display information requested by user via user interface
def delivery_status_one_package(input_time, hashmap, packageID) -> None:
    package1 = hashmap.find_package(packageID)
    if input_time < package1.time_loaded:
        if package1.ID == 9:
            package1.address = '300 State St'
        print(f'Package ID: {package1.ID} | '
                f'Destination: {package1.address} {package1.city} {package1.state} {package1.zipcode} | '
                f'Deadline: {package1.deadline} | '
                f'Weight: {package1.weight} kilograms | '
                f'Truck: {package1.truck} | '
                f'Status: At Hub\n')
        if package1.ID == 9:
            package1.address = '410 S State St'
    elif input_time > package1.time_loaded and input_time < package1.delivery_time:
        print(f'Package ID: {package1.ID} | '
               f'Destination: {package1.address} {package1.city} {package1.state} {package1.zipcode} | '
               f'Deadline: {package1.deadline} | '
               f'Weight: {package1.weight} kilograms | '
               f'Truck: {package1.truck} | '
               f'Status: In Transit\n')
    elif input_time > package1.delivery_time:
        print(f'Package ID: {package1.ID} | '
               f'Destination: {package1.address} {package1.city} {package1.state} {package1.zipcode} | '
               f'Deadline: {package1.deadline} | '
               f'Weight: {package1.weight} kilograms | '
               f'Truck: {package1.truck} | '
               f'Status: Delivered at {package1.delivery_time}\n')
    return

# Requirement D
# Prints total mileage of all trucks
print(f"Total mileage for today's deliveries: {round(total_mileage, 1)}")

# Requirement D
# This block allows users to interface with the program to query package status at given times
print('To navigate the program please follow the prompts exactly.  Any invalid inputs will result in the program closing.')
try:
    while True:
        numerical_input = input('Please choose from the following options:\n'
                                '1. Display all delivered packages from today\n'
                                '2. Display status of all packages at a specific time\n'
                                '3. Display status of individual package at a specific time\n'
                                '4. Exit \n')
        if numerical_input == '1':
            try:
                for i in range (1, number_of_packages + 1):
                    found_package = package_hash_map.find_package(i)
                    found_package.print_package()
                    print('')
            except ValueError:
                print('Input invalid. Exiting.')
                exit()
        elif numerical_input == '2':
            try:
                time = input('Please choose the time for which you would like the status of all packages\n'
                             'Enter your time in hh:mm format:'
                             '\n')
                (hours, minutes) = time.split(":")

                time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(hours), int(minutes), 0, 0)
                delivery_status_from_time(time, package_hash_map)
            except ValueError:
                print('Input invalid. Exiting.')
                exit()


        elif numerical_input == '3':
            try:
                time = input('Please choose the time for which you would like the status of your package\n'
                             'Enter your time in hh:mm format:\n')
                (hours, minutes) = time.split(":")
                time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(hours), int(minutes), 0, 0)

                package_id = int(input('Please input the package ID for your package:\n'))

                delivery_status_one_package(time, package_hash_map, package_id)
            except ValueError:
                print('Input invalid. Exiting.')
                exit()

        elif numerical_input == '4':
            exit()

        else:
            try:
                print('Input invalid. Exiting.')
                exit()

            except ValueError:
                print('Input invalid. Exiting.')
                exit()

except KeyboardInterrupt:
    print('\nProgram terminated by user')
