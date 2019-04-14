import readFile as rf

def bubbleSort(list):
    for i in range(len(list), 0, -1):
        for j in range(0, i-1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]

# test = [6,2,3,99,1,3,5,6,7,10,8]

test = rf.getNumberDataList()

bubbleSort(test)
print(test)