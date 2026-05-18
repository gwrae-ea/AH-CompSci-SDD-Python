class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.__startDate = str(startDate)  #String
        self.__startTime = str(startTime)  #String
        self.__venue = str(venue)          #String
        self.__reminder = reminder if isinstance(reminder, bool) else str(reminder).strip().lower() in ("true", "1", "yes", "y")    #Boolean (don't use bool(reminder): bool("False") is True)
        self.__participants = [""]*20 #Array of String
        self.__index = int(0)              #Integer

    def updateDate(self, eventDate):
        self.__startDate = str(eventDate)

    def getDate(self):
        return self.__startDate

    def getVenue(self):
        if 5 <= len(self.__venue) <= 15:
            return self.__venue
        return "Invalid venue"

    def getParticipants(self):
        return self.__participants

    def getParticipantCount(self):
        return self.__index

    def addParticipant(self, name):
        self.__participants[self.__index] = str(name)
        self.__index = self.__index + 1

# Valid venue test
item1 = Event("13/04/18", "0900", "Main Hall", True)
print("Valid venue:", item1.getVenue())

# Too-short venue test
item2 = Event("13/04/18", "0900", "Gym", True)
print("Too-short venue:", item2.getVenue())

# Too-long venue test
item3 = Event("13/04/18", "0900", "International Conference Centre", True)
print("Too-long venue:", item3.getVenue())

# Date update test
print("Original date:", item1.getDate())
item1.updateDate("14/04/22")
print("Updated date:", item1.getDate())

# Participant tests
item1.addParticipant("Erica Knowles")
item1.addParticipant("Norman Osborne")
print("Participant count:", item1.getParticipantCount())
print("Participants:", item1.getParticipants())

# Direct access test
try:
    print(item1.__venue)
except AttributeError:
    print("Direct access blocked; use getVenue() instead")
