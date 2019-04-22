import multiprocessing
from functools import reduce

def multiProcessRunSort(dataList, sortFunc, mergeMultiList = None, targetListLen = 0):
    if (mergeMultiList == None):
        mergeMultiList = defaultMergeMultiList
    if (targetListLen < 1):
        targetListLen = int(len(dataList) ** 0.5)

    dataList = splitRun(dataList, sortFunc, mergeMultiList, targetListLen)
    return dataList

def defaultMergeMultiList(multiList):
    newList = [0] * reduce((lambda x, y: x + len(y)), multiList, 0)
    for i in range(len(newList)):
        newList[i] = multiList[i%len(multiList)][i//len(multiList)]
    return newList



def splitRun(dataList, sortFunc, mergeMultiList, targetListLen):
    topNode = splitListToTargetListLen(dataList, targetListLen)
    sortForEveryDataList(topNode, sortFunc)
    mergeAllNodeToTop(topNode, mergeMultiList)

    dataList = topNode.list
    return dataList


def defaultProcessNumber():
    return multiprocessing.cpu_count()

class Pool:
    _instance = None
    def __init__():
        return Pool.getPool()

    def getPool():
        if (Pool._instance == None):
            Pool._instance = multiprocessing.Pool(defaultProcessNumber())
        return Pool._instance


class Node:
    def __init__(self, dataList = [], topNode = None):
        self.list = dataList
        self.top = topNode

    def isData(self):
        return type(self.list[0]) is not Node


def splitListToTargetListLen(dataList, targetListLen):
    topNode = Node()
    topNode.list = splitListToNodeList(dataList, topNode)
    deepList = getDeepList(topNode)
    while (len(deepList[-1].list) > targetListLen):
        for node in deepList:
            node.list = splitListToNodeList(node.list, node)
        deepList = getDeepList(topNode)
    return topNode

def sortForEveryDataList(topNode, sortFunc):
    pool = Pool.getPool()
    deepList = getDeepList(topNode)
    sortList = pool.map(sortFunc, getListFromNodeList(deepList))
    for i in range(len(deepList)):
        deepList[i].list = sortList[i]
    return topNode

def mergeAllNodeToTop(topNode, mergeMultiList):
    pool = Pool.getPool()
    while (not topNode.isData()):
        deepList = getDeepList(topNode, 1)
        newList = getListFromNodeList(deepList)
        for i in range(len(newList)):
            newList[i] = getListFromNodeList(newList[i])
        mergedLists = pool.map(mergeMultiList, newList)
        for i in range(len(deepList)):
            deepList[i].list = mergedLists[i]
    return topNode



def getDeepList(multiNodeList, top = 0):
    deepList = multiNodeList.list
    while (not deepList[0].isData()):
        newDeepList = []
        for node in deepList:
            newDeepList.extend(node.list)
        deepList = newDeepList

    while (top > 0):
        topList = []
        for node in deepList:
            if (node.top not in topList):
                topList.append(node.top)
        deepList = topList
        top -= 1

    return deepList

def getListFromNodeList(nodeList):
    newList = []
    for node in nodeList:
        newList.append(node.list)
    return newList

def splitListToNodeList(dataList, top = None):
    nodeList = splitList(dataList)
    for i in range(len(nodeList)):
        nodeList[i] = Node(nodeList[i], top)
    return nodeList

def splitList(dataList):
    multiDataList = []
    for i in range(defaultProcessNumber()):
        multiDataList.append([])
    for i in range(len(dataList)):
        multiDataList[i%len(multiDataList)].append(dataList[i])
    return multiDataList
