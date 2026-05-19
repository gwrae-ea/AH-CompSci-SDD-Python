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
        return self.__venue

    def addParticipant(self, name):
        self.__participants[self.__index] = str(name)
        self.__index = self.__index + 1

class WorkMeeting(Event):
    def __init__(self, startDate, startTime, venue, reminder, meetingTitle, mileage):
        super().__init__(startDate, startTime, venue, reminder)
        self.__meetingTitle = str(meetingTitle)      #String
        self.__mileage = float(mileage)              #Real
        self.__travelExpenses = float(0)             #Real

    def calculateTravelExpenses(self):
        self.__travelExpenses = self.__mileage * 1.5
    
    def getTravelExpenses(self):
        return self.__travelExpenses