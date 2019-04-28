import multiprocessing
from .multiProcessRunSort import multiProcessRunSort, defaultMergeMultiList
from .bubbleSort import bubbleSort

def multiBubbleSort(dataList):
    dataList = multiProcessRunSort(dataList, bubbleSort, mergeMultiList)

    return dataList

def mergeMultiList(multiList):
    return bubbleSort(defaultMergeMultiList(multiList))
