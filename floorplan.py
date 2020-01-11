

class RoomInfo:
    def __init__(self, roomId, people):
        self.name = roomId
        self.occupants = people

class Room:
    def __init__(self, oRooms = [], people = [], sensors = [], roomId = 0):
        self.oRooms = oRooms
        self.people = people
        self.sensors = sensors
        self.roomId = roomId

    def seeInfo(self):
        return RoomInfo(self.roomID, self.people)

    def updateRoom(self, nPeople):
        for person in nPeople:
            if person in self.people:
                self.people.remove(person)
            else:
                self.people.append(person)
    


class FloorPlan:
    def __init__(self, startRoom, building = None):
        self.building = building
        self.floorMap = self.buildMap(dict(), startRoom)

    def getInfo(self):
        return self.floorMap

    def updateFP(self, roomId, people):
        if roomId in floorMap.keys():
            floorMap[roomId].updateRoom(people)
        else:
            print("Error could not find that room")
        return

    def buildMap(self, floorMap, startRoom):
        for room in startRoom.oRooms:
            if room.roomId in floorMap:
                continue
            floorMap[room.roomId] = room
            self.buildMap(floorMap, room)
        return floorMap
    def prettyPrint(self):
        pass

a = Room([],[],[], 100)
b = Room([a],[],[], 101)
c = Room([a,b],[], [], 102)
a.oRooms.append(b)
a.oRooms.append(c)
b.oRooms.append(c)
test = FloorPlan(a, "RH")
print(test)
