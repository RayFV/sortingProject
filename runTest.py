import time
import readFile as rf

def runTest(name, sortFunc, sortArgs = {}, printResult = False, testTimes = 10):
    print("start test sort [ " + name  + " ], test times: " + str(testTimes))
    originData = rf.getNumberDataList()
    testData = originData.copy()

    startTime = time.time()
    for i in range(testTimes):
        testData = originData.copy()
        sortFunc(testData, **sortArgs)
    endTime = time.time()
    spendTime = endTime - startTime

    if (printResult):
        print(testData)
    print(" end  test sort [ " + name + " ], spend time: " + str(spendTime))
    print()
