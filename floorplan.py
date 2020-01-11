def class room:
    def __init__(self, oRooms = [], people = [], sensors = [], id = 0):
        self.oRooms = oRooms
        self.people = people
        self.sensors = sensors
        self.id = id

    def seeRooms(self):
        return self.oRooms
    
    def seePeople(self):
        return self.people
    
    def seeSensors(self):
        return self.sensors

    def roomid(self):
        return self.id

    

