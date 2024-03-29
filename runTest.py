import time
import readFile as rf
from checkAnswer import checkAnswer, setAnswer

def runTest(name, sortFunc, sortArgs = {}, printResult = False, testTimes = 1,baseAnswer=False):
    originData = rf.getNumberDataList()
    testData = []
    print("start test sort [ " + name  + " ], test times: " + str(testTimes) + ", length of list: " + str(len(originData)))

    startTime = time.time()
    for _ in range(testTimes):
        testData = originData.copy()
        result = sortFunc(testData, **sortArgs)
        if (result != None):
            testData = result
    endTime = time.time()
    spendTime = endTime - startTime

    mins = int(spendTime // 60)
    secs = spendTime % 60
    print(" end  test sort [ " + name + " ], spend time: " + str(mins) + " mins, " + str(secs) + " secs")

    if (printResult):
        print(testData)

    if(baseAnswer):
        setAnswer(testData)

    if (not checkAnswer(testData)):
        print("** error")
        print("** this sort function get wrong answer **")
        print("** error")
    print()
