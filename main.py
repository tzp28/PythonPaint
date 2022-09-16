class Home:
    def __init__(self):
        self.rooms = []

    def addRoom(self, name):
        self.rooms.append(name)


class Room:
    def __init__(self, walls, name):
        self.walls = walls
        self.name = name


class Wall:
    def __init__(self, height, width, windows, doors):
        self.height = height
        self.width = width
        self.height = windows
        self.width = doors


if __name__ == '__main__':
    roomNum = input("Enter the amount of rooms in your home: ")
    userHouse = Home()
    for room in range(int(roomNum)):
        roomName = input("Enter the name of room {}: ".format(room+1))
        userHouse.addRoom(roomName)
        roomName = input("Enter the # of walls in " + roomName + ": ")

    print(userHouse.rooms)


