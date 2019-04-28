import readFile as rf
from runTest import *
from sortAlgorithm.bubbleSort import bubbleSort
from sortAlgorithm.insertionSort import insertionSort
from sortAlgorithm.quickSort import quickSort
from sortAlgorithm.radixSort import radixSort
from sortAlgorithm.selectionSort import selectionSort
from sortAlgorithm.shellSort import shellSort
from sortAlgorithm.countingSort import countingSort
from sortAlgorithm.mergeSort import mergeSort
from sortAlgorithm.heapSort import heapSort
from sortAlgorithm.multiBubbleSort import multiBubbleSort
from sortAlgorithm.multiInsertionSort import multiInsertionSort
from sortAlgorithm.multiMergeSort import multiMergeSort
from sortAlgorithm.multiSelectionSort import multiSelectionSort

def main():
    testData = rf.getNumberDataList()

    runTest("countingSort", countingSort,baseAnswer=True)

    runTest("radixSort", radixSort, { "radix": 1000 })
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
