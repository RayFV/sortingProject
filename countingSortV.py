import time
from countingSort import countingSort

FILENAME = "Test.dat"

def runTest():
    startTime = time.time()
    print("start [ countingSort ]")

    testData = []
    dataFile = open(FILENAME,"r")
    for line in dataFile:
        splitedList = line.split(" ")
        del splitedList[-1] #remove '\n'
        testData += splitedList

    dataFile.close()
    
    testData = list(map(int, testData)) # convert to int
    countingSort(testData)

    endTime = time.time()
    spendTime = endTime - startTime

    mins = int(spendTime // 60)
    secs = spendTime % 60
    print(" end [ countingSort ], spend time: " + str(mins) + " mins, " + str(secs) + " secs")


runTest()
