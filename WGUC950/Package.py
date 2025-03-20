# Creates Package class and defines attributes and methods
from datetime import datetime


class Package(object):
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status) -> None:

        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.time_loaded = None
        self.delivery_time = None
        self.truck = None

        return

    # Returns ID of a package
    def get_id(self) -> int:
        ID = self.ID
        return ID

    # Returns address of a package
    def get_address(self) -> str:
        address = self.address
        return address

    # Updates delivery status of package
    def update_status(self, ID: int, status: str) -> None:
        self.ID = ID
        self.status = status
        return

    # Gives package a delivery time based on delivery algorithm
    def update_delivery_time(self, ID: int, delivery_time):
        self.ID = ID
        self.delivery_time = delivery_time
        return

    # Gives package a truck ID corresponding to truck it is loaded on
    def update_truck(self, truck_ID):
        self.truck = truck_ID
        return

    # Parses deadline to a datetime object
    # Used to check against delivery time in main file
    def parse_deadline(self) -> datetime:
        if self.deadline == "EOD":
            deadline = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 0, 0, 0)
        else:
            deadline_string = self.deadline
            deadline_string = deadline_string[:5]
            (hours, minutes) = deadline_string.split(":")
            deadline = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(hours), int(minutes), 0, 0)
        return deadline

    # Prints all info about a package
    def print_package(self) -> None:
        print(f'Package ID: {self.ID} | '
              f'Destination: {self.address} {self.city} {self.state} {self.zipcode} | '
              f'Deadline: {self.deadline} | '
              f'Delivery Time: {self.delivery_time} | '
              f'Weight: {self.weight} kilograms | '
              f'Truck: {self.truck} | '
              f'Status: {self.status}')
        return

