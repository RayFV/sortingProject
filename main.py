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
from multiBubbleSort import multiBubbleSort
from multiInsertionSort import multiInsertionSort
from multiMergeSort import multiMergeSort
from multiSelectionSort import multiSelectionSort

def main():
    testData = rf.getNumberDataList()

    runTest("countingSort", countingSort,baseAnswer=True)

    runTest("radixSort", radixSort)
    runTest("quickSort", quickSort, { "lowIndex": 0, "highIndex": len(testData) - 1 })
    runTest("heapSort", heapSort)
    runTest("mergeSort", mergeSort)
    runTest("shellSort", shellSort)
    runTest("multi core MergeSort", multiMergeSort)
    runTest("multi core SelectionSort", multiSelectionSort)
    runTest("multi core InsertionSort", multiInsertionSort)
    runTest("multi core BubbleSort", multiBubbleSort)

    # runTest("insertionSort", insertionSort)
    # runTest("selectionSort", selectionSort)
    # runTest("bubbleSort", bubbleSort)

if __name__ == "__main__":
    main()
