class Car():
#define the structure and content of the City Record
    def __init__( self, car_id,car_make,car_model,car_colour,car_year,car_serviced ):
        self.car_id = car_id #String
        self.car_make = car_make #String
        self.car_model = car_model #String
        self.car_colour = car_colour #String
        self.car_year = car_year #String
        self.car_serviced = car_serviced #String

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
            if cArray[i].car_make > cArray[i+1].car_make:
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
        if target == cA[mid].car_make:
            position = mid
            found = True
        elif target >= cA[mid].car_make:
            low = mid + 1
        else:
            high = mid - 1
    
    return position
    
carArray = readFileToArrayOfObjects()

print ("*Unsorted Array*")
for cars in range (0,len(carArray)):
    print (carArray[cars].car_make)

sortedArray = bubbleSortArrayofObjects(carArray)

print ("*Unsorted Array*")
for cars in range (0,len(carArray)):
    print (carArray[cars].car_make)


target = str(input("What make of car are you looking for? "))
position = binarySearch(sortedArray, target)
if position == -1:
    print ("Sorry, we don't have any of that make.")
else:
    print ("Yes! We have that make of car!")
