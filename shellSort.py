def shellSort(dataList):
    gap = len(dataList) // 2
    while (gap > 1):
        _insertionSort(dataList, gap)
        gap = gap // 2
    _insertionSort(dataList, 1)

def _insertionSort(dataList, gap = 1):
    startIndex = gap
    while (startIndex < gap*2):
        i = startIndex
        while (i < len(dataList)):
            currentNumber = dataList[i]
            j = i - gap
            while ((j >= 0) and (dataList[j] > currentNumber)):
                dataList[j + gap] = dataList[j]
                j -= gap
            dataList[j + gap] = currentNumber
            i += gap
        startIndex += 1
