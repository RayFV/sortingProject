import multiprocessing
from functools import reduce
from insertionSort import insertionSort

def defaultProcessNumber():
    return multiprocessing.cpu_count()

def multiInsertionSort(dataList, processNumber=0):
    pool = multiprocessing.Pool()
    dataList = splitRun(pool, dataList, int(len(dataList) ** 0.5))

    return dataList

def splitRun(pool, dataList, targetListLen = 10000):
    multiDataList = []
    for i in range(defaultProcessNumber()):
        multiDataList.append([])
    for i in range(len(dataList)):
        multiDataList[i%len(multiDataList)].append(dataList[i])

    if (len(multiDataList[-1]) > targetListLen):
        return mergeMultiList(list(map((lambda l: splitRun(pool, l, targetListLen)), multiDataList)))
    else:
        return mergeMultiList(pool.map(insertionSort, multiDataList))

def mergeMultiList(multiList):
    newList = [0] * reduce((lambda x, y: x + len(y)), multiList, 0)
    for i in range(len(newList)):
        newList[i] = multiList[i%len(multiList)][i//len(multiList)]
    return insertionSort(newList)
