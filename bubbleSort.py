def bubbleSort(dataList):
    for i in range(len(dataList), 0, -1):
        changeFlag = False
        for j in range(0, i-1):
            if(dataList[j] > dataList[j+1]):
                dataList[j], dataList[j+1] = dataList[j+1], dataList[j]
                changeFlag = True
        if (not changeFlag):
            break
    return dataList
