def bubbleSort(nA):

    n = len(nA)
    swapped = True

    while swapped and n>=0:
        swapped = False
        for i in range(0,n-1): #changed from algorithm (n-2)
            if nA[i] > nA[i+1]:
                temp = numArray[i]
                nA[i] = nA [i+1]
                nA[i+1] = temp
                swapped = True
        n = n-1
    return nA

def binarySearch(nA, target):
    low = 0
    high =  len(nA)-1
    mid = 0
    found = False
    position = -1

    while not(found) and low <= high:
        mid = int((low + high)/2)
        if target == nA[mid]:
            position = mid
            found = True
        elif target >= nA[mid]:
            low = mid + 1
        else:
            high = mid - 1     
    
    return position 

numArray = [23,546,2,3214,456,234,3214,4576,4657,324,321,4658,765,324,6548,435,54687,32,46857,87659,435,486,87690,5]
numArray = bubbleSort(numArray)
print (numArray)
posFound = binarySearch(numArray,int(input("Please enter value to find: ")))
print (posFound)
