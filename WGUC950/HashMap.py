from Package import Package

# Requirement A
# Creates HashMap object and defines attributes and methods
class HashMap(object):
    def __init__(self, size = 10) -> None:
        self.size = size
        self.hashMap = []
        for i in range(self.size):
            self.hashMap.append([])
        return

    # Returns index of item in HashMap from Key input
    def get_index(self, ID: int) -> int:
        index = hash(ID) % len(self.hashMap)
        return index

    # Adds a new item to HashMap
    def add_package(self, package: Package) -> None:
        ID = package.get_id()
        index = self.get_index(ID)
        index_list = self.hashMap[index]
        index_list.append([ID, package])
        return

    # Updates a package already in HashMap
    def update_package(self, package: Package) -> None:
        ID = package.get_id()
        index = self.get_index(ID)
        index_list = self.hashMap[index]
        for i in index_list:
            if i[0] == ID:
                i[1] = package
        return

    # Returns an item given a Key input
    def find_package(self, ID):
        index = self.get_index(ID)
        for i in self.hashMap[index]:
            if i[0] == ID:
                return i[1]
        return

