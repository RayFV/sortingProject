import readFile as rf
from runTest import *
from bubbleSort import bubbleSort
from quickSort import quickSort
from radixSort import radixSort

def main():
    testData = rf.getNumberDataList()

    runTest("bubbleSort", bubbleSort)
    runTest("quickSort", quickSort, { "lowIndex": 0, "highIndex": len(testData) - 1 })
    runTest("radixSort", radixSort)

main()
