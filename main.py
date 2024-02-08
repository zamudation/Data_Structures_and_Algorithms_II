# Isaac Zamudio Zarraga  Student ID: 001333192

from Trucks import loadTrucks
from Package import getPackageTable
import Delivering
import datetime

# This function will load the trucks' ad be ready for the delivering part
loadTrucks()
print("------------------------------------------------------")
print("Welcome to the route delivery tucks algorithm.")
print("------------------------------------------------------")

# This executes the delivering and prints the total miles traveled by the trucks
print("The program has been executed and every package has been delivered.\n"
      "The total distance traveled by all the trucks is a total of : {} miles.".format(Delivering.getTotalDistance()))
print("------------------------------------------------------")

selection = 'null'

# Starts the menu selection and will do what the user decides to do
while selection != '3':

    selection = input("Menu\n"
                      " From the next options select what yo want to do:\n"
                      "  1. Print the information of all packages.\n"
                      "  2. Print the information of a specific package. \n"
                      "  3. Exit the program.\n")

    # Prints the information of all the packages at a specific time
    if selection == '1':

        try:
            inputTime = input("Please enter a time with this format (hh:mm:ss) : ")
            (hrs, min, sec) = inputTime.split(':')
            inTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))

            print("\nPackages:")

            # This sections prepares the time in order to determine where the packages are
            for i in range(len(getPackageTable().table) + 30):
                deliverTime = getPackageTable().search(i + 1)[10]
                (hrs, min, sec) = deliverTime.split(':')
                delTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))
                startTime = getPackageTable().search(i + 1)[9]
                (hrs, min, sec) = startTime.split(':')
                stTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))
                if delTime > inTime > stTime:
                    status = "In route"
                elif inTime >= delTime > stTime:
                    status = f" Delivered at {getPackageTable().search(i + 1)[10]}"
                else:
                    status = "At Hub"

                # Prints the information
                print(f"ID: {getPackageTable().search(i + 1)[0]} "
                      f"Address: {getPackageTable().search(i + 1)[2]} "
                      f"City: {getPackageTable().search(i + 1)[3]} "
                      f"Zip: {getPackageTable().search(i + 1)[5]} "
                      f"Weight: {getPackageTable().search(i + 1)[7]} "
                      "Status: " + status)
        except ValueError:

            print("\n______Invalid input. Start again from the Menu______\n")

    # This selection allows the user to print the information of a specific package at a specific time
    elif selection == '2':
        try:

            # Verifies that the user selects an existing package
            packageId = input("Type the package ID that you want information about (1 to 40): ")
            if 1 <= int(packageId) <= 40:
                inputTime = input("Please enter a time with this format (hh:mm:ss) : ")
                (hrs, min, sec) = inputTime.split(':')
                inTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))

                # This sections prepares the times in order to determine where the package is
                deliverTime = getPackageTable().search(int(packageId))[10]
                (hrs, min, sec) = deliverTime.split(':')
                delTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))
                startTime = getPackageTable().search(int(packageId))[9]
                (hrs, min, sec) = startTime.split(':')
                stTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))
                if delTime > inTime > stTime:
                    status = "In route"
                elif inTime >= delTime > stTime:
                    status = f" Delivered at {getPackageTable().search(int(packageId))[10]}"
                else:
                    status = "At Hub"

                # Prints the information about the package
                print(f"\nID: {getPackageTable().search(int(packageId))[0]} \n"
                      f"Address: {getPackageTable().search(int(packageId))[2]} \n"
                      f"City: {getPackageTable().search(int(packageId))[3]} \n"
                      f"Zip: {getPackageTable().search(int(packageId))[5]} \n"
                      f"Weight: {getPackageTable().search(int(packageId))[7]} \n"
                      "Status: " + status + "\n")

            else:
                print("\n______Invalid input. Start again from the Menu______\n")
        except ValueError:
            print("\n______Invalid input. Start again from the Menu______\n")
    elif selection == '3':
        exit()
    else:
        print("Input not in the menu, please select a valid option\n")
