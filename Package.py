import csv
from HashTable import ChainingHashTable

# Create an instance of my Chaining Hash Table
myPackageHash = ChainingHashTable()


# Reads the CSV file and adds the list of packages to my hash table
with open('Documents/Packages.csv') as packages:
    packagesData = csv.reader(packages, delimiter=',')

    for package in packagesData:
        pID = int(package[0])
        pAddress = package[1]
        pCity = package[2]
        pState = package[3]
        pZip = package[4]
        pDelivery = package[5]
        pMass_kg = package[6]
        pNotes = package[7]
        pAddressID = ''
        pStartTime = ''
        pStatus = 'At Hub'

        # package object
        p = [pID, pAddressID, pAddress, pCity, pState, pZip, pDelivery, pMass_kg, pNotes, pStartTime, pStatus]

        # insert it into the hash table
        myPackageHash.insert(pID, p)


def getPackageTable():
    return myPackageHash
