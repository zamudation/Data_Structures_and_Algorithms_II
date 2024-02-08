import csv
from HashTable import ChainingHashTable

# Creates a hash table that holds all the addresses
myAddressHash = ChainingHashTable()

# Opens the address file to add all of them to the hash table
with open('Documents/Addresses.csv') as addresses:
    addressesData = csv.reader(addresses, delimiter=',')

    for address in addressesData:
        aID = int(address[0])
        aAddress = address[1]
        aZip = address[2]

        # address object
        a = [aID, aAddress, aZip]

        # insert it into the hash table
        myAddressHash.insert(aID, a)


def getAddressTable():
    return myAddressHash
