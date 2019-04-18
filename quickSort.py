import readFile as rf

def quickSort(dataList, lowIndex, highIndex):
    if lowIndex >= highIndex:
        return

    pivot = dataList[highIndex]
    headIndex = lowIndex
    for i in range(lowIndex, highIndex+1):
        if(dataList[i] <= pivot):
            dataList[i], dataList[headIndex] = dataList[headIndex], dataList[i]
            headIndex += 1

    quickSort(dataList, lowIndex, headIndex-2)
    quickSort(dataList, headIndex, highIndex)
