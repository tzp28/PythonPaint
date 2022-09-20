class Home:
    def __init__(self):
        self.rooms = []

    def addRoom(self, name):
        self.rooms.append(name)


class Room:
    def __init__(self):
        self.walls = []

    def addWall(self, name):
        self.walls.append(name)


class Wall:
    def __init__(self, height, width, windows, doors, area):
        self.height = height
        self.width = width
        self.windows = windows
        self.doors = doors
        self.area = area


if __name__ == '__main__':
    units = input("Which units do you use for length? (Enter Imperial or Metric, please): ")
    if units == "Imperial":
        units = "sq ft"
    if units == "Metric":
        units = "sq meters"
    roomNum = input("Enter the amount of rooms in your home: ")
    userHouse = Home()
    userRoom = Room()
    roomSurArea = 0
    totSurArea = 0
    totWinArea = 0
    totDoorArea = 0
    totalCost = 0
    for room in range(int(roomNum)):
        roomName = input("Enter the name of room {}: ".format(room + 1))
        userHouse.addRoom(roomName)
        wallNum = input("Enter the # of walls in " + roomName + ": ")
        for wall in range(int(wallNum)):
            wallHeight = input("Enter the height of the wall " + str(wall + 1) + ": ")
            wallWidth = input("Enter the width of the wall " + str(wall + 1) + ": ")
            wallWindows = input("Enter the # of windows on wall " + str(wall + 1) + ": ")
            if int(wallWindows) > 0:
                for window in range(int(wallWindows)):
                    windowHeight = input("Enter the height of the window " + str(window + 1) + ": ")
                    windowWidth = input("Enter the width of the window " + str(window + 1) + ": ")
                    windowArea = int(windowHeight) * int(windowWidth)
                    totWinArea += windowArea
            else:
                totWinArea = 0
            wallDoors = input("Enter the # of doors on wall " + str(wall + 1) + ": ")
            if int(wallDoors) > 0:
                for door in range(int(wallDoors)):
                    doorHeight = input("Enter the height of the door " + str(door + 1) + ": ")
                    doorWidth = input("Enter the width of the door " + str(door + 1) + ": ")
                    doorArea = int(doorHeight) * int(doorWidth)
                    totDoorArea += doorArea
            else:
                totDoorArea = 0
            wallArea = ((int(wallHeight) * int(wallWidth)) - totWinArea - totDoorArea)
            userWall = Wall(wallHeight, wallWidth, wallWindows, wallDoors, wallArea)
            userRoom.addWall(userWall)
            # print(userWall.height, userWall.width, userWall.windows, userWall.doors, userWall.area)
            print("")
            roomSurArea += userWall.area
            print("The Surface Area for wall " + str(wall + 1) + " is: " + str(userWall.area) + " " + units)
        paintCeiling = input("Do you want to paint the ceiling (Enter Yes or No, please): ")
        if paintCeiling == "Yes":
            ceilingHeight = int(input("Enter the length of the ceiling: "))
            ceilingWidth = int(input("Enter the width of the ceiling: "))
            ceilingArea = ceilingHeight * ceilingWidth
        if paintCeiling == "No":
            ceilingHeight = 0
            ceilingWidth = 0
            ceilingArea = 0
        roomSurArea += ceilingArea
        totSurArea += roomSurArea
        print("The Surface Area for " + roomName + " is: " + str(roomSurArea) + " " + units)
        print("")
        coats = int(input("How many coats of paint do you want for " + roomName + ": "))
        if units == "sq ft":
            print((roomSurArea * coats) / 400)
            gallons = round((roomSurArea * coats) / 400, 0)
            print("You need at least " + str(gallons) + " gallons to paint all of " + roomName)
            print(
                f"Available Paints: Behr White - ${24.99 * gallons}, Glidden Blue - ${32.99 * gallons}, PPG Grey - ${29.99 * gallons}")
            roomPaint = input("Enter the available paint for " + roomName + ": ")
            roomCost = 0
            if roomPaint == "Behr White":
                roomCost = round(24.99 * gallons,2)
                print("To paint the " + roomName + " it will cost: $" + str(roomCost))
                totalCost += roomCost
                print("The total cost so far is: $" + str(totalCost))
            if roomPaint == "Glidden Blue":
                roomCost = round(32.99 * gallons,2)
                print("To paint the " + roomName + " it will cost: $" + str(roomCost))
                totalCost += roomCost
                print("The total cost so far is: $" + str(totalCost))
            if roomPaint == "PPG Grey":
                roomCost = round(29.99 * gallons,2)
                print("To paint the " + roomName + " it will cost: $" + str(roomCost))
                totalCost += roomCost
                print("The total cost so far is: $" + str(totalCost))
        if units == "sq meters":
            units = "sq meters"

    print("")
    if units == "sq ft":
        print(
            "To paint your home with the total surface area of " + str(totSurArea) + " square ft with " + str(
                gallons) + "gallons of paint it will "
                           "cost $" + str(totalCost))
    # print("Select the Paint Brand" + roomName + ": ")
    # print("Select the brand of " + roomName + ": ")
    # print(userHouse.rooms)
    # print(userRoom.walls)
