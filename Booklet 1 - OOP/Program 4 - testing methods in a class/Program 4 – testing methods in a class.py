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

#Test for the CONSTRUCTOR method
item1 = Event("13/04/18", "0900", "Main Office", True)
print (item1.venue)

#Test the updateDate() method by showing original date
#then showing the new date
print (item1.startDate, "is the original date")
item1.updateDate("13/04/22")
print (item1.startDate, "is the updated date")

#Test the getDate() method by printing the returned value
print (item1.getDate(), "is the date from the getDate() method")

#Test the addParticipant() method is allocating names and incrementing index
print (item1.index)
print (item1.participants)
item1.addParticipant ("Erica Knowles")
item1.addParticipant ("Norman Osborne")
item1.addParticipant ("Fred Savage")
print (item1.index)
print (item1.participants)
