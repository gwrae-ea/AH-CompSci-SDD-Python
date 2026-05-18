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
