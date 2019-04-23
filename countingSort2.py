# 可以Handle負數

def countingSort2(dataList):
    max_number, min_number = find_max_and_min(dataList)

    temp = [0] * (max_number - min_number + 1)
    
    count(dataList, temp, min_number)
    
    modify(temp)

    sort(dataList, temp, min_number)
    
def find_max_and_min(dataList):
    max = dataList[0]
    
    min = dataList[0]
    
    for i in dataList:
        if i > max:
            max = i

        if i < min:
            min = i
            
    return max, min
    
def count(dataList, temp, min_number):
    for i in dataList:
        temp[i - min_number] = temp[i - min_number] + 1
        
def modify(temp):
    for i, d in enumerate(temp):
        if i > 0:
            temp[i] = temp[i - 1] + d
            
def sort(dataList, temp, min_number):
    copy = dataList.copy()
    
    for i in copy:
        dataList[temp[i - min_number] - 1] = i
        temp[i - min_number] = temp[i - min_number] - 1
        
