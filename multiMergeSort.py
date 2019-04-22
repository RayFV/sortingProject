import multiprocessing
from functools import reduce
from multiProcessRunSort import multiProcessRunSort

def multiMergeSort(dataList, splitNumber = 16):
    # 依照 merge sort 的原始定義, splitNumber 應設為 2, 即每次切 2 份
    # 但設為 16 會有更加的效能, 即每次切 16 份
    dataList = multiProcessRunSort(dataList, sortFunc, mergeMultiList, targetListLen = 1, splitNumber = splitNumber, shouldSort = False)

    return dataList

def sortFunc(dataList):
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
