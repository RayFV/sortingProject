import time
import readFile as rf
from checkAnswer import checkAnswer

def runTest(name, sortFunc, sortArgs = {}, printResult = False, testTimes = 1):
    print("start test sort [ " + name  + " ], test times: " + str(testTimes))
    originData = rf.getNumberDataList()
    testData = originData.copy()

    startTime = time.time()
    for _ in range(testTimes):
        testData = originData.copy()
        sortFunc(testData, **sortArgs)
    endTime = time.time()
    spendTime = endTime - startTime

    if (printResult):
        print(testData)
    print(" end  test sort [ " + name + " ], spend time: " + str(spendTime) + " sec")
    if (not checkAnswer(testData)):
        print("** error")
        print("** this sort function get wrong answer **")
        print("** error")
    print()
