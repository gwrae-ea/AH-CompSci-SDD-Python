class Car():
#define the structure and content of the City Record
    def __init__( self, car_id,car_make,car_model,car_colour,car_year,car_serviced ):
        self.car_id = str(car_id) #String
        self.car_make = str(car_make) #String
        self.car_model = str(car_model) #String
        self.car_colour = str(car_colour) #String
        self.car_year = str(car_year) #String
        self.car_serviced = str(car_serviced) #String

    def get_car_id(self):
        return self.car_id

    def get_car_make(self):
        return self.car_make

    def get_car_model(self):
        return self.car_model

    def get_car_colour(self):
        return self.car_colour

    def get_car_year(self):
        return self.car_year

    def get_car_serviced(self):
        return self.car_serviced

    def set_car_make(self, car_make):
        self.car_make = str(car_make)

    def set_car_model(self, car_model):
        self.car_model = str(car_model)

    def set_car_colour(self, car_colour):
        self.car_colour = str(car_colour)

    def set_car_year(self, car_year):
        self.car_year = str(car_year)

    def set_car_serviced(self, car_serviced):
        self.car_serviced = str(car_serviced)

def readFileToArrayOfObjects():

    cArray = []
    entireFile = open ( "dataFiles/carData.csv" , "r" )
    #this file needs to be in the same folder as the program
    linesArray = entireFile.read().splitlines()
    entireFile.close()
    for line in linesArray:
        lineSplit = line.split( "," )
        currentCar = Car(lineSplit[0], lineSplit[1], lineSplit[2],lineSplit[3],lineSplit[4],lineSplit[5])
        cArray.append(currentCar)
    return cArray 


def bubbleSortArrayofObjects(cArray):
    n = len(cArray)
    swapped = True

    while swapped and n>=0:
        swapped = False
        for i in range(0,n-1): #changed from algorithm (n-2)
            if cArray[i].get_car_make() > cArray[i+1].get_car_make():
                temp = cArray[i]
                cArray[i] = cArray [i+1]
                cArray[i+1] = temp
                swapped = True
        n = n-1
    return cArray

def binarySearch(cA, target):
    low = 0
    high =  len(cA)-1
    mid = 0
    found = False
    position = -1

    while not(found) and low <= high:
        mid = int((low + high)/2)
        if target == cA[mid].get_car_make():
            position = mid
            found = True
        elif target >= cA[mid].get_car_make():
            low = mid + 1
        else:
            high = mid - 1
    
    return position
    
carArray = readFileToArrayOfObjects()

print ("*Unsorted Array*")
for cars in range (0,len(carArray)):
    print (carArray[cars].get_car_make())

sortedArray = bubbleSortArrayofObjects(carArray)

print ("*Sorted Array*")
for cars in range (0,len(carArray)):
    print (carArray[cars].get_car_make())


target = str(input("What make of car are you looking for? "))
position = binarySearch(sortedArray, target)
if position == -1:
    print ("Sorry, we don't have any of that make.")
else:
    print ("Yes! We have that make of car!")
