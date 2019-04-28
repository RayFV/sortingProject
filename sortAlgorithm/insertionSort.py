def insertionSort(dataList):
    i = 1
    while (i < len(dataList)):
        currentNumber = dataList[i]
        j = i - 1
        while ((j >= 0) and (dataList[j] > currentNumber)):
            dataList[j + 1] = dataList[j]
            j -= 1
        dataList[j + 1] = currentNumber
        i += 1
    return dataList
