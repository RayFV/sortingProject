import multiprocessing
from functools import reduce
from selectionSort import selectionSort

def multiSelectionSort(dataList, processNumber=0):
    # if (processNumber < 1):
    #     processNumber = defaultProcessNumber()
    # multiDataList = []
    # for i in range(processNumber):
    #     multiDataList.append([])
    # for i in range(len(dataList)):
    #     multiDataList[i%len(multiDataList)].append(dataList[i])

    # pool = multiprocessing.Pool()
    # multiDataList = pool.map(selectionSort, multiDataList)
    # dataList = mergeMultiList(multiDataList)

    pool = multiprocessing.Pool()
    dataList = splitRun(pool, dataList)

    return dataList

def defaultProcessNumber():
    return multiprocessing.cpu_count()

def splitRun(pool, dataList):
    multiDataList = []
    for i in range(defaultProcessNumber()):
        multiDataList.append([])
    for i in range(len(dataList)):
        multiDataList[i%len(multiDataList)].append(dataList[i])

    if (len(multiDataList[-1]) > 10000):
        return mergeMultiList(list(map((lambda l: splitRun(pool, l)), multiDataList)))
    else:
        return mergeMultiList(pool.map(selectionSort, multiDataList))



def findMinList(multiDataList):
    multiDataList = list(filter(lambda l: len(l) > 0, multiDataList))
    minList = multiDataList[0]
    for i in range(1, len(multiDataList)):
        if (multiDataList[i][0] < minList[0]):
            minList = multiDataList[i]
    return minList

def mergeMultiList(multiList):
    newList = [0] * reduce((lambda x, y: x + len(y)), multiList, 0)
    for i in range(len(newList)):
        minList = findMinList(multiList)
        newList[i] = minList[0]
        del minList[0]
    return newList
