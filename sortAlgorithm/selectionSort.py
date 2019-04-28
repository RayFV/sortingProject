def selectionSort(dataList):
    dataListLen = len(dataList)
    for i in range(dataListLen - 1):
        minIndex = i
        for j in range(i + 1, dataListLen):
            if (dataList[j] < dataList[minIndex]):
                minIndex = j
        if (minIndex != i):
            minNumber = dataList[minIndex]
            dataList[minIndex] = dataList[i]
            dataList[i] = minNumber
    return dataList
