def heapSort(dataList):
    heap_tree = build_heap_tree(dataList)

    dataList[:] = sort(heap_tree)
    
def build_heap_tree(dataList):
    heap_tree = []

    for i, d in enumerate(dataList):
        heap_tree.append(d)
    
        while i > 0:
            if heap_tree[i] < heap_tree[int((i - 1) / 2)]:
                
                heap_tree[i], heap_tree[int((i - 1) / 2)] = heap_tree[int((i - 1) / 2)], heap_tree[i]
                
                i = int((i - 1) / 2)

            else:
                break
    
    return heap_tree
    
def sort(dataList):
    ans = []

    while len(dataList) > 0:
        dataList[0], dataList[-1] = dataList[-1], dataList[0]
        
        ans.append(dataList.pop())
        
        root = 0
        
        while True:
            if len(dataList) > root * 2 + 2:
                min_index = root * 2 + 1 if dataList[root * 2 + 1] < dataList[root * 2 + 2] else root * 2 + 2
                
                if dataList[root] > dataList[min_index]:
                    dataList[root], dataList[min_index] = dataList[min_index], dataList[root]
                
                    root = min_index
                    
                else:
                    break
                
            elif len(dataList) > root * 2 + 1:
                if dataList[root] > dataList[root * 2 + 1]:
                    dataList[root], dataList[root * 2 + 1] = dataList[root * 2 + 1], dataList[root]
                
                else:
                    break
                    
            else:
                break
    
    return ans
    