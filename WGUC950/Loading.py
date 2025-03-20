# Module that handles functions that load packages
import csv

from Package import Package
from Truck import Truck
from HashMap import HashMap

# Takes a HashMap object and CSV file and adds all packages from file into HashMap
def load_package(file: csv, hashmap) -> None:
    with open(file) as csv_data:
        package_data = csv.reader(csv_data, delimiter=',')
        for row in package_data:
            package_id = int(row[0])
            package_address = row[1]
            package_city = row[2]
            package_state = row[3]

            package_zipcode = row[4]
            package_deadline_time = row[5]
            package_weight = row[6]
            package_status = "At Hub"

            package = Package(package_id, package_address, package_city, package_state, package_zipcode,
                              package_deadline_time, package_weight, package_status)
            hashmap.add_package(package)

    return

# Updates packages in HashMap object based on the truck they are assigned to
# Updates time, status and assigns a truck ID
def load_packages_to_truck(truck: Truck, packages: list[int], hashmap: HashMap) -> None:
    for package in packages:
        updated_package = hashmap.find_package(package)
        Package.update_status(updated_package, package, "En Route")
        Package.update_truck(updated_package, truck.get_ID())
        updated_package.time_loaded = truck.time
        hashmap.update_package(updated_package)
        truck.packages.append(package)

    return
