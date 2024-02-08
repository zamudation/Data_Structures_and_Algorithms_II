import csv
import datetime

firstDelivery = [0]
secondDelivery = [0]
thirdDelivery = [0]

# This list is created to keep all the times of when each package is delivered, and it's used to add them to the main
# package hash table
firstDeliveryTime = ['8:00:00']
secondDeliveryTime = ['9:15:00']
thirdDeliveryTime = ['11:00:00']

truckOne = []
truckTwo = []
truckThree = []

# Reads the distances and keep a list of all them, keeping them as a table
with open('Documents/Distance.csv') as distances:
    distancesData = list(csv.reader(distances, delimiter=','))

    # Gets the total distance of the different trucks when the function is called
    def getTraveledDistance(row, col, total):
        if distancesData[row][col] == '':
            distance = distancesData[col][row]
        else:
            distance = distancesData[row][col]
        return total + float(distance)

    # Gets the distance between two points and its used when the program is trying to find the shortest path
    def getDistanceBetweenTwoPoints(row, col):
        if distancesData[row][col] == '':
            distance = distancesData[col][row]
        else:
            distance = distancesData[row][col]
        return float(distance)

    # This function find the amount of time a truck takes to fet from one point to another
    def getTime(distance, startTime):
        addingTimeMinutes = int((60 * distance) / 18)
        addingTimeSeconds = ((60 * distance) % 18) * 60
        addTime = datetime.timedelta(minutes=addingTimeMinutes, seconds=addingTimeSeconds)
        (hrs, min, sec) = startTime.split(':')
        startTime = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))
        finalTime = startTime + addTime

        return finalTime

    # This is the function I choose to deliver my packages, and it's the shortest route function
    def getShortestRoute(TruckList, startLocation, truck):
        if not len(TruckList):
            return TruckList

        # random number to start the for statements that is bigger than any other distance
        lowestValue = 20

        # For loop to find the shortest path of in the truck list
        for i in TruckList:
            addressId = i[1]
            if getDistanceBetweenTwoPoints(startLocation, addressId) <= lowestValue:
                lowestValue = getDistanceBetweenTwoPoints(startLocation, addressId)
                newLocation = addressId

        # For loop to append the order of delivery packages of each truck in a list
        for i in TruckList:
            if getDistanceBetweenTwoPoints(startLocation, i[1]) == lowestValue:
                if truck == 1:
                    firstDelivery.append(i[1])
                    truckOne.append(i)
                elif truck == 2:
                    secondDelivery.append(i[1])
                    truckTwo.append(i)
                elif truck == 3:
                    thirdDelivery.append(i[1])
                    truckThree.append(i)
                TruckList.pop(TruckList.index(i))

                # This call keep the function running until there are not more packages are left and every package is
                # order to be delivered in the shortest path possible
                getShortestRoute(TruckList, newLocation, truck)


    def getTotalDistance():
        # This three lines add the address of the hub at the end of the sorted list of address of each truck
        firstDelivery.append(0)
        secondDelivery.append(0)
        thirdDelivery.append(0)

        totalDistanceOne = 0
        totalDistanceTwo = 0
        totalDistanceThree = 0

        # This section gets the total distance traveled by truck one and fills the delivery times for the delivery
        # time of truck one
        for i in range(len(firstDelivery) - 1):
            totalDistanceOne = getTraveledDistance(firstDelivery[i], firstDelivery[i + 1], totalDistanceOne)
            deliveredTime = getTime(getDistanceBetweenTwoPoints(firstDelivery[i], firstDelivery[i + 1]),
                                    firstDeliveryTime[i])

            firstDeliveryTime.append(str(deliveredTime))

        # This section gets the total distance traveled by truck two and fills the delivery times for the delivery
        # time of truck two
        for i in range(len(secondDelivery) - 1):
            totalDistanceTwo = getTraveledDistance(secondDelivery[i], secondDelivery[i + 1], totalDistanceTwo)
            deliveredTime = getTime(getDistanceBetweenTwoPoints(secondDelivery[i], secondDelivery[i + 1]),
                                    secondDeliveryTime[i])

            secondDeliveryTime.append(str(deliveredTime))

        # This section gets the total distance traveled by truck three and fills the delivery times for the delivery
        # time of truck three
        for i in range(len(thirdDelivery) - 1):
            totalDistanceThree = getTraveledDistance(thirdDelivery[i], thirdDelivery[i + 1], totalDistanceThree)
            deliveredTime = getTime(getDistanceBetweenTwoPoints(thirdDelivery[i], thirdDelivery[i + 1]),
                                    thirdDeliveryTime[i])

            thirdDeliveryTime.append(str(deliveredTime))

        # Adds the delivery times for the packages in truck number one
        for i in range(len(truckOne)):
            truckOne[i][10] = firstDeliveryTime[i+1]

        # Adds the delivery times for the packages in truck number two
        for i in range(len(truckTwo)):
            truckTwo[i][10] = secondDeliveryTime[i+1]

        # Adds the delivery times for the packages in truck number three
        for i in range(len(truckThree)):
            truckThree[i][10] = thirdDeliveryTime[i+1]

        # gets the total distance traveled by all trucks
        totalDistance = totalDistanceOne + totalDistanceTwo + totalDistanceThree
        return float(totalDistance)


    def getFirstDeliveryIds():
        return firstDelivery


    def getSecondDeliveryIds():
        return secondDelivery


    def getThirdDeliveryIds():
        return thirdDelivery
