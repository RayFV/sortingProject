FILENAME = "Test.dat"

isLimit = True
limit = 500 #數量

def getNumberDataList():
    allData = []
    dataFile = open(FILENAME,"r")
    for line in dataFile:
        if(isLimit and isOverLimit(len(allData))):
            break
            
        splitedList = line.split(" ")
        del splitedList[-1] #remove '\n'
        allData += splitedList

    dataFile.close()
    return list(map(int, allData)) # convert to int


def isOverLimit(length):
    return length > limit
