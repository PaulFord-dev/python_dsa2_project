import Distance
import HashMap

from datetime import datetime, timedelta

# Creates Truck class and defines attributes and methods
class Truck(object):
    def __init__(self, ID: int) -> None:
        self.ID = ID
        self.location = "4001 South 700 East"
        self.packages = []
        self.mileage = 0.0
        self.time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8, 0, 0, 0)
        return

    # Returns list of packages assigned to truck
    def get_packages(self) -> list:
        return self.packages

    # Returns address of most recent truck location
    def get_location(self) -> str:
        return self.location

    # Returns truck ID
    def get_ID(self) -> int:
        return self.ID

    # Updates address to trucks most recent location
    def update_location(self, location: str) -> None:
        self.location = location
        return

    # Updates mileage of truck
    def update_mileage(self, mileage: float) -> None:
        self.mileage = self.mileage + mileage
        return

    # Updates time
    def update_time(self, time_delta) -> None:
        self.time = self.time + timedelta(minutes=time_delta)

    # Takes package ID off of package list for truck
    def remove_package(self, ID) -> None:
        self.packages.remove(ID)
        return

    # Finds the closest address of packages from package list
    def least_distance(self, address_list: list, distance_list: list, hashmap: HashMap) -> int:
        packages = self.get_packages()
        location = self.get_location()
        closest = float('inf')
        next_package_ID = None
        for package in packages:
            next_package = hashmap.find_package(package)
            address = next_package.get_address()
            distance = float(Distance.get_distances(address, location, address_list, distance_list))
            if distance < closest:
                closest = distance
                next_package_ID = package

        return next_package_ID

    # Algorithm that finds next closest package and updates package list, truck and HashMap accordingly
    def deliver_packages(self, address_list: list, distance_list: list, hashmap: HashMap) -> None:
        while len(self.packages) > 0:
            next_package_ID = self.least_distance(address_list, distance_list, hashmap)
            next_package = hashmap.find_package(next_package_ID)
            distance = float(Distance.get_distances(self.get_location(), next_package.get_address(), address_list, distance_list))
            next_package.update_status(next_package_ID, "Delivered")
            self.update_mileage(distance)
            self.update_location(next_package.get_address())
            self.update_time(distance/.3)
            # print(self.time)
            next_package.update_delivery_time(next_package_ID, self.time)
            hashmap.update_package(next_package)
            # next_package.print_package()
            self.remove_package(next_package_ID)
            # print(self.packages)
            # print(self.mileage)
            # print(self.location)
        distance = float(Distance.get_distances(self.get_location(), "4001 South 700 East", address_list, distance_list))
        self.update_mileage(distance)
        self.update_location("4001 South 700 East")
        self.update_time(distance/.3)
        # print(self.packages)
        # print(self.mileage)
        # print(self.location)
        # print(self.time)
        return

