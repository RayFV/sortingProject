import readFile as rf

def bubbleSort(dataList):
    for i in range(len(dataList), 0, -1):
        for j in range(0, i-1):
            if(dataList[j] > dataList[j+1]):
                dataList[j], dataList[j+1] = dataList[j+1], dataList[j]

# test = [6,2,3,99,1,3,5,6,7,10,8]

test = rf.getNumberDataList()

bubbleSort(test)
print(test)