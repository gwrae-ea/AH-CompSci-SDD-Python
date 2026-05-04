class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.startDate = startDate  #String
        self.startTime = startTime  #String
        self.venue = venue          #String
        self.reminder = reminder    #Boolean
        self.participants = [""]*20 #Array of String
        self.index = 0              #Integer

    def updateDate(self, eventDate):
        self.startDate  = eventDate

    def getDate(self):
        return self.startDate

    def addParticipant(self, name):
        self.participants[self.index] = name
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