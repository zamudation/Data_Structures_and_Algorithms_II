from Package import getPackageTable
from Delivering import getShortestRoute
import Address

truckOne = []
truckTwo = []
truckThree = []

# These are added to the delivery list as the first address, since that where all the trucks  depart from
firstDeliveryAddressId = [0]
secondDeliveryAddressId = [0]
thirdDeliveryAddressId = [0]


def loadTrucks():
    # Loading truck 1
    truckOne.append(getPackageTable().search(1))
    truckOne.append(getPackageTable().search(13))
    truckOne.append(getPackageTable().search(14))
    truckOne.append(getPackageTable().search(15))
    truckOne.append(getPackageTable().search(16))
    truckOne.append(getPackageTable().search(20))
    truckOne.append(getPackageTable().search(29))
    truckOne.append(getPackageTable().search(30))
    truckOne.append(getPackageTable().search(31))
    truckOne.append(getPackageTable().search(34))
    truckOne.append(getPackageTable().search(37))
    truckOne.append(getPackageTable().search(40))

    # Loading truck 2
    truckTwo.append(getPackageTable().search(3))
    truckTwo.append(getPackageTable().search(6))
    truckTwo.append(getPackageTable().search(17))
    truckTwo.append(getPackageTable().search(18))
    truckTwo.append(getPackageTable().search(21))
    truckTwo.append(getPackageTable().search(23))
    truckTwo.append(getPackageTable().search(25))
    truckTwo.append(getPackageTable().search(26))
    truckTwo.append(getPackageTable().search(28))
    truckTwo.append(getPackageTable().search(32))
    truckTwo.append(getPackageTable().search(33))
    truckTwo.append(getPackageTable().search(36))
    truckTwo.append(getPackageTable().search(38))
    truckTwo.append(getPackageTable().search(39))

    # Loading truck 3
    truckThree.append(getPackageTable().search(2))
    truckThree.append(getPackageTable().search(4))
    truckThree.append(getPackageTable().search(5))
    truckThree.append(getPackageTable().search(7))
    truckThree.append(getPackageTable().search(8))
    truckThree.append(getPackageTable().search(9))
    truckThree.append(getPackageTable().search(10))
    truckThree.append(getPackageTable().search(11))
    truckThree.append(getPackageTable().search(12))
    truckThree.append(getPackageTable().search(19))
    truckThree.append(getPackageTable().search(22))
    truckThree.append(getPackageTable().search(24))
    truckThree.append(getPackageTable().search(27))
    truckThree.append(getPackageTable().search(35))

    # Add the starting time for first truck
    for i in range(len(truckOne)):
        truckOne[i][9] = '8:00:00'

    # Add the starting time for second truck
    for i in range(len(truckTwo)):
        truckTwo[i][9] = '9:15:00'

    # Add the starting time for third truck
    for i in range(len(truckThree)):
        truckThree[i][9] = '11:00:00'

    # Compares the packages on first truck and then adds ID of that address to the package on Truck
    for package in truckOne:
        for address in range(len(Address.getAddressTable().table) + 17):
            if package[2] == Address.getAddressTable().search(address)[1]:
                package[1] = Address.getAddressTable().search(address)[0]

    # Compares the packages on second truck and then adds ID of that address to the package on Truck
    for package in truckTwo:
        for address in range(len(Address.getAddressTable().table) + 17):
            if package[2] == Address.getAddressTable().search(address)[1]:
                package[1] = Address.getAddressTable().search(address)[0]

    # Compares the packages on third truck and then adds ID of that address to the package on Truck
    for package in truckThree:
        for address in range(len(Address.getAddressTable().table) + 17):
            if package[2] == Address.getAddressTable().search(address)[1]:
                package[1] = Address.getAddressTable().search(address)[0]

    # Calls sortTruckAddresses() function
    sortTruckAddresses()


def sortTruckAddresses():

    # Sorts all the packages from the trucks to the shortest route for each
    getShortestRoute(truckOne, 0, 1)
    getShortestRoute(truckTwo, 0, 2)
    getShortestRoute(truckThree, 0, 3)


def getTruckOne():
    return truckOne


def getTruckTwo():
    return truckTwo


def getTruckThree():
    return truckThree
