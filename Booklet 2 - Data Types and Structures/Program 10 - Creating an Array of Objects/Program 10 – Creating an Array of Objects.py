class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.startDate = str(startDate)  #String
        self.startTime = str(startTime)  #String
        self.venue = str(venue)          #String
        self.reminder = reminder if isinstance(reminder, bool) else str(reminder).strip().lower() in ("true", "1", "yes", "y")    #Boolean (don't use bool(reminder): bool("False") is True)
        self.participants = [""]*20 #Array of String
        self.index = int(0)              #Integer

    def updateDate(self, eventDate):
        self.startDate  = str(eventDate)

    def getDate(self):
        return self.startDate

    def addParticipant(self, name):
        self.participants[self.index] = str(name)
        self.index = self.index + 1

#Creating and populating an Array of Objects
eventArray = [''] * 20
eventArray[0] = Event("14/04/2022", "0900", "Main Office", True )
eventArray[1] = Event("15/04/2022", "1030", "Staff Room", True )

eventArray[1].addParticipant("Erica Knowles")
print (eventArray[1].participants)
