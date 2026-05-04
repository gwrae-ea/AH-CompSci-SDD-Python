class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.__startDate = startDate  #String
        self.__startTime = startTime  #String
        self.__venue = venue          #String
        self.__reminder = reminder    #Boolean
        self.__participants = [""]*20 #Array of String
        self.__index = 0              #Integer

    def updateDate(self, eventDate):
        self.startDate  = eventDate

    def getDate(self):
        return self.startDate

    def addParticipant(self, name):
        self.participants[self.index] = name
        self.index = self.index + 1

class WorkMeeting(Event):
    def __init__(self, startDate, startTime, venue, reminder, meetingTitle, mileage ):
        super().__init__(startDate, startTime, venue, reminder)
        self.meetingTitle = meetingTitle      #String
        self.mileage = mileage                #Real
        self.travelExpenses = 0               #Real

    def calculateTravelExpenses(self):
        self.travelExpenses = self.mileage * 1.5
    
    def getTravelExpenses(self):
        return self.travelExpenses