def bubbleSort(nA):

    n = len(nA)
    swapped = True

    while swapped and n>=0:
        swapped = False
        for i in range(0,n-1): #changed from algorithm (n-2)
            if nA[i] > nA[i+1]:
                temp = nA[i]
                nA[i] = nA [i+1]
                nA[i+1] = temp
                swapped = True
        n = n-1
    return (nA)

numArray = [23,546,2,3214,456,234,321]
print (numArray)
numArray = bubbleSort(numArray) #if you want to keep the original array, assign to a new array at this point
print (numArray)
