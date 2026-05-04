def insertionSort(nA):
    value = 0
    index = 0
    for i in range (1, len(nA)): #changed from algorithm (len(nA)-1)
        value = nA[i]
        index = i
        while index > 0 and value < nA[index-1]:
            nA[index] = nA[index-1]
            index = index - 1
        nA[index] = value
    return (nA)

numArray = [23,546,2,3214,456,234,321 ]
sortedArray = insertionSort(numArray)
print (sortedArray)
