def class room:
    def __init__(self, oRooms = [], people = [], sensors = [], id = 0):
        self.oRooms = oRooms
        self.people = people
        self.sensors = sensors
        self.id = id

    def seeInfo(self):
        return [self.oRooms, self.people, self.sensors, self.id]
    
   
    

