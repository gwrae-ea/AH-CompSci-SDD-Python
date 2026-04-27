class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.date = startDate       #String
        self.startTime = startTime  #String
        self.venue = venue          #String
        self.reminder = reminder    #Boolean
        self.participants = [""]*20 #Array of String
        self.index = 0              #Integer


item1 = Event("13/04/18", "0900", "Main Office", True)
print (item1.venue)
