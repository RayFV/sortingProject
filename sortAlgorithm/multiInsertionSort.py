import multiprocessing
from .multiProcessRunSort import multiProcessRunSort, defaultMergeMultiList
from .insertionSort import insertionSort

def multiInsertionSort(dataList):
    dataList = multiProcessRunSort(dataList, insertionSort, mergeMultiList)

    return dataList

def mergeMultiList(multiList):
    return insertionSort(defaultMergeMultiList(multiList))
