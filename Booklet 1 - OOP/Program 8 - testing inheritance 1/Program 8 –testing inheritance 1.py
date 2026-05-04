class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.__startDate = startDate  #String
        self.__startTime = startTime  #String
        self.__venue = venue          #String
        self.__reminder = reminder    #Boolean
        self.__participants = [""]*20 #Array of String
        self.__index = 0              #Integer

    def updateDate(self, eventDate):
        self.__startDate = eventDate

    def getDate(self):
        return self.__startDate

    def addParticipant(self, name):
        self.__participants[self.__index] = name
        self.__index = self.__index + 1

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

#Test for the CONSTRUCTOR method (inheriting from Event class)
workMeeting1 = WorkMeeting(startDate = "14/04/21", startTime = "0900", venue = "Main Office", reminder = True, meetingTitle = "Work from Home", mileage = 7.5)

print ("The date of the meeting was" , workMeeting1.getDate())
