import multiprocessing
from functools import reduce
from .multiProcessRunSort import multiProcessRunSort
from .selectionSort import selectionSort

def multiSelectionSort(dataList):
    dataList = multiProcessRunSort(dataList, selectionSort, mergeMultiList)

    return dataList

def mergeMultiList(multiList):
    newList = [0] * reduce((lambda x, y: x + len(y)), multiList, 0)
    for i in range(len(newList)):
        minList = findMinList(multiList)
        newList[i] = minList[0]
        del minList[0]
    return newList

def findMinList(multiDataList):
    multiDataList = list(filter(lambda l: len(l) > 0, multiDataList))
    minList = multiDataList[0]
    for i in range(1, len(multiDataList)):
        if (multiDataList[i][0] < minList[0]):
            minList = multiDataList[i]
    return minList
