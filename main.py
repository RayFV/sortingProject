import readFile as rf
from runTest import *
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from quickSort import quickSort
from radixSort import radixSort
from selectionSort import selectionSort
from shellSort import shellSort
from countingSort import countingSort
from mergeSort import mergeSort
from heapSort import heapSort

def main():
    testData = rf.getNumberDataList()

    runTest("bubbleSort", bubbleSort)
    runTest("quickSort", quickSort, { "lowIndex": 0, "highIndex": len(testData) - 1 })
    runTest("radixSort", radixSort)

    runTest("insertionSort", insertionSort)
    runTest("selectionSort", selectionSort)
    runTest("shellSort", shellSort)

    runTest("countingSort", countingSort)
    runTest("mergeSort", mergeSort)
    runTest("heapSort", heapSort)

main()
