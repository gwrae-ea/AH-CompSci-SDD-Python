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

def populateEventArrayFromFile():
    eA = []
    entireFile = open("dataFiles/eventData.csv", "r")
    linesArray = entireFile.read().splitlines()
    entireFile.close()
    for line in linesArray:
        lineSplit = line.split(",")
        currentEvent = Event(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
        eA.append(currentEvent)
    return eA

#Creating and populating an Array of Objects
eventArray = populateEventArrayFromFile()
print (eventArray[0].venue)
print (eventArray[23].startTime)