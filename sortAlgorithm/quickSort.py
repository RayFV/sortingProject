def quickSort(dataList, lowIndex, highIndex):
    while lowIndex < highIndex:

        pivot = dataList[highIndex]
        headIndex = lowIndex
        for i in range(lowIndex, highIndex+1):
            if(dataList[i] <= pivot):
                dataList[i], dataList[headIndex] = dataList[headIndex], dataList[i]
                headIndex += 1

        if (headIndex - lowIndex < highIndex - headIndex):
            quickSort(dataList, lowIndex, headIndex - 2)
            lowIndex = headIndex
        else:
            quickSort(dataList, headIndex, highIndex)
            highIndex = headIndex - 2

