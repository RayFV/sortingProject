def countingSort(dataList):
    max_number = find_max(dataList)
    temp = [0] * (max_number + 1)
    count(dataList, temp)
    modify(temp)
    sort(dataList, temp)


def find_max(dataList):
    max = dataList[0]

    for i in dataList:
        if i > max:
            max = i

    return max


def count(dataList, temp):
    for i in dataList:
        temp[i] = temp[i] + 1


def modify(temp):
    for i, d in enumerate(temp):
        if i > 0:
            temp[i] = temp[i - 1] + d


def sort(dataList, temp):
    copy = dataList.copy()

    for i in copy:
        dataList[temp[i] - 1] = i
        temp[i] = temp[i] - 1

