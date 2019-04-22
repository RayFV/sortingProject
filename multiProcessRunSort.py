import multiprocessing
from functools import reduce

class Pool:
    _instance = None
    def __init__():
        return Pool.getPool()

    def getPool():
        if (Pool._instance == None):
            Pool._instance = multiprocessing.Pool()
        return Pool._instance

def multiProcessRunSort(dataList, sortFunc, mergeMultiList = None, targetListLen = 0):
    if (mergeMultiList == None):
        mergeMultiList = defaultMergeMultiList
    if (targetListLen < 1):
        targetListLen = int(len(dataList) ** 0.5)

    dataList = splitRun(dataList, sortFunc, mergeMultiList, targetListLen)
    return dataList

def splitRun(dataList, sortFunc, mergeMultiList, targetListLen):
    multiDataList = []
    for i in range(defaultProcessNumber()):
        multiDataList.append([])
    for i in range(len(dataList)):
        multiDataList[i%len(multiDataList)].append(dataList[i])

    if (len(multiDataList[-1]) > targetListLen):
        return mergeMultiList(list(map((lambda l: splitRun(l, sortFunc, mergeMultiList, targetListLen)), multiDataList)))
    else:
        pool = Pool.getPool()
        return mergeMultiList(pool.map(sortFunc, multiDataList))

def defaultProcessNumber():
    return multiprocessing.cpu_count()

def defaultMergeMultiList(multiList):
    newList = [0] * reduce((lambda x, y: x + len(y)), multiList, 0)
    for i in range(len(newList)):
        newList[i] = multiList[i%len(multiList)][i//len(multiList)]
    return newList
