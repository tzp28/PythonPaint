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


class Paint:
    def __init__(self, store, brand, color, cost):
        self.store = store
        self.brand = brand
        self.color = color
        self.cost = cost

    def setPaint(self, store, brand, color):
        if store == 'Home Depot':
            if brand == 'Behr':
                self.cost = 12.99
            if brand == 'Glidden':
                self.cost = 9.99
            if brand == 'PPG':
                self.cost = 7.99
            if brand == 'Behr' or brand == 'Glidden' or brand == 'PPG':
                if color == 'White':
                    self.cost += 10
                if color == 'Red':
                    self.cost += 20
                if color == 'Grey':
                    self.cost += 15
                if color == 'Blue':
                    self.cost += 20
                if color == 'Neutral':
                    self.cost += 12
                if color == 'Pink':
                    self.cost += 22

        if store == 'B&Q':
            if brand == 'GoodHome':
                self.cost = 2.49
            if brand == 'Dulux':
                self.cost = 4.99
            if brand == 'Leyland':
                self.cost = 1.49
            if brand == 'GoodHome' or brand == 'Dulux' or brand == 'Leyland':
                if color == 'White':
                    self.cost += 1
                if color == 'Red':
                    self.cost += 2
                if color == 'Grey':
                    self.cost += 1.5
                if color == 'Blue':
                    self.cost += 2
                if color == 'Neutral':
                    self.cost += 1.2
                if color == 'Pink':
                    self.cost += 2.2


def unitSystem():
    while True:
        units = input("Which units do you use for length? (Enter Imperial or Metric, please): ")
        if units == "Imperial":
            units = "sq ft"
            return units
        if units == "Metric":
            units = "sq meters"
            return units
        else:
            print("Please enter Imperial or Metric")


if __name__ == '__main__':
    userHouse = Home()
    userRoom = Room()
    stores = ['Home Depot', 'B&Q']
    brands = ['Behr', 'Glidden', 'PPG', 'GoodHome', 'Dulux', 'Leyland']
    colors = ['White', 'Red', 'Grey', 'Blue', 'Neutral', 'Pink', 'Green']
    userPaint = Paint(stores, brands, colors, 0)

    roomSurArea = 0
    totSurArea = 0
    totWinArea = 0
    totDoorArea = 0
    totalCost = 0
    totGallons = 0
    totLitres = 0
    units = unitSystem()
    roomNum = input("Enter the amount of rooms in your home: ")

    for room in range(int(roomNum)):
        roomSurArea = 0
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
                    windowArea = float(windowHeight) * float(windowWidth)
                    totWinArea += windowArea
            else:
                totWinArea = 0
            wallDoors = input("Enter the # of doors on wall " + str(wall + 1) + ": ")
            if int(wallDoors) > 0:
                for door in range(int(wallDoors)):
                    doorHeight = input("Enter the height of the door " + str(door + 1) + ": ")
                    doorWidth = input("Enter the width of the door " + str(door + 1) + ": ")
                    doorArea = float(doorHeight) * float(doorWidth)
                    totDoorArea += doorArea
            else:
                totDoorArea = 0
            wallArea = ((float(wallHeight) * float(wallWidth)) - totWinArea - totDoorArea)
            userWall = Wall(wallHeight, wallWidth, wallWindows, wallDoors, wallArea)
            userRoom.addWall(userWall)
            # print(userWall.height, userWall.width, userWall.windows, userWall.doors, userWall.area)
            print("")
            roomSurArea += userWall.area
            print("The Surface Area for wall " + str(wall + 1) + " is: " + str(userWall.area) + " " + units)
        paintCeiling = input("Do you want to paint the ceiling (Enter Yes or No, please): ")
        if paintCeiling == "Yes":
            ceilingHeight = float(input("Enter the length of the ceiling: "))
            ceilingWidth = float(input("Enter the width of the ceiling: "))
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
            # print((roomSurArea * coats) / 400)
            gallons = round((roomSurArea * coats) / 400, 0)
            print("You need at least " + str(gallons) + " gallons to paint all of " + roomName)
            totGallons += gallons
            while True:
                userPaint.cost = 0
                print("Available Brands from Home Depot: " + str(userPaint.brand[0:3]))
                print("Available Colors from Home Depot: " + str(userPaint.color))
                userBrand = input("Enter a available Brand from Home Depot: ")
                # print(userPaint.cost)
                userColor = input("Enter an available Color from Home Depot: ")
                userPaint.setPaint('Home Depot', userBrand, userColor)
                roomCost = 0
                roomCost = round(int(userPaint.cost), 2)
                # print(roomCost)
                print("The cost for " + userBrand + " " + userColor + f" is ${roomCost} per gallon")
                roomCost = roomCost * gallons
                print("To paint the " + roomName + " it will cost: $" + str(roomCost))
                selectPaint = input(
                    "Do you want to select " + userBrand + " " + userColor + " as your paint for the " + roomName + " (Enter, Y/N please): ")

                if selectPaint == "Y":
                    totalCost += roomCost
                    print("The total cost so far is: $" + str(totalCost))
                    break

                if selectPaint == "N":
                    print("")
                else:
                    print("Please Enter Y or N")
        if units == "sq meters":
            # print((roomSurArea * coats) / 48)
            litres = round((roomSurArea * coats) / 48, 0)
            print("You need at least " + str(litres) + " litres to paint all of " + roomName)
            totLitres += litres
            while True:
                userPaint.cost = 0
                print("Available Brands from B&Q: " + str(userPaint.brand[3:6]))
                print("Available Colors from B&Q: " + str(userPaint.color))
                userBrand = input("Enter a available Brand from B&Q: ")
                # print(userPaint.cost)
                userColor = input("Enter an available Color from B&Q: ")
                userPaint.setPaint('B&Q', userBrand, userColor)
                roomCost = 0
                roomCost = round(int(userPaint.cost), 2)
                # print(roomCost)
                print("The cost for " + userBrand + " " + userColor + f" is £{roomCost} per litres")
                roomCost = roomCost * litres
                print("To paint the " + roomName + " it will cost: £" + str(roomCost))
                selectPaint = input(
                    "Do you want to select " + userBrand + " " + userColor + " as your paint for the " + roomName + " (Enter, Y/N please): ")

                if selectPaint == "Y":
                    totalCost += roomCost
                    print("The total cost so far is: £" + str(totalCost))
                    break

                if selectPaint == "N":
                    print("")
                else:
                    print("Please Enter Y or N")

    print("")
    if units == "sq ft":
        print(
            "To paint your home with the total surface area of " + str(totSurArea) + " square ft with " + str(
                totGallons) + " gallons of paint it will "
                              "cost $" + str(totalCost))

    if units == "sq meters":
        print(
            "To paint your home with the total surface area of " + str(totSurArea) + " square meters with " + str(
                totLitres) + " litres of paint it will "
                             "cost £" + str(totalCost))
