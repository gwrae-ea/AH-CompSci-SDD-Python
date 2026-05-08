class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.__startDate = str(startDate)  #String
        self.__startTime = str(startTime)  #String
        self.__venue = str(venue)          #String
        self.__reminder = reminder if isinstance(reminder, bool) else str(reminder).strip().lower() in ("true", "1", "yes", "y")    #Boolean (don't use bool(reminder): bool("False") is True)
        self.__participants = [""]*20 #Array of String
        self.__index = int(0)              #Integer

    def updateDate(self, eventDate):
        self.startDate  = str(eventDate)

    def getDate(self):
        return self.startDate

    def addParticipant(self, name):
        self.participants[self.index] = str(name)
        self.index = self.index + 1

class WorkMeeting(Event):
    def __init__(self, startDate, startTime, venue, reminder, meetingTitle, mileage ):
        super().__init__(startDate, startTime, venue, reminder)
        self.meetingTitle = str(meetingTitle)      #String
        self.mileage = float(mileage)                #Real
        self.travelExpenses = float(0)               #Real

    def calculateTravelExpenses(self):
        self.travelExpenses = self.mileage * 1.5
    
    def getTravelExpenses(self):
        return self.travelExpenses


#Test for the CONSTRUCTOR method (inheriting from Event class)
workMeeting1 = WorkMeeting(startDate = "14/04/21", startTime = "0900", venue = "Main Office", reminder = True, meetingTitle = "Work from Home", mileage = 7.5)

#Test for the 2 methods in WorkMeeting class
print ("Before calculation, the travel expenses are £", workMeeting1.getTravelExpenses())
workMeeting1.calculateTravelExpenses()
print ("After calculation, the travel expenses are £", workMeeting1.getTravelExpenses())
