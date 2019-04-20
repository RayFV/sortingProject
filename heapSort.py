def heapSort(list):
    heap_tree = build_heap_tree(list)

    return sort(heap_tree)
    
def build_heap_tree(list):
    heap_tree = []

    for i, d in enumerate(list):
        heap_tree.append(d)
    
        while i > 0:
            if heap_tree[i] < heap_tree[int((i - 1) / 2)]:
                
                heap_tree[i], heap_tree[int((i - 1) / 2)] = heap_tree[int((i - 1) / 2)], heap_tree[i]
                
                i = int((i - 1) / 2)

            else:
                break
    
    return heap_tree
    
def sort(list):
    ans = []

    while len(list) > 0:
        list[0], list[-1] = list[-1], list[0]
        
        ans.append(list.pop())
        
        root = 0
        
        while True:
            if len(list) > root * 2 + 2:
                min_index = root * 2 + 1 if list[root * 2 + 1] < list[root * 2 + 2] else root * 2 + 2
                
                if list[root] > list[min_index]:
                    list[root], list[min_index] = list[min_index], list[root]
                
                    root = min_index
                    
                else:
                    break
                
            elif len(list) > root * 2 + 1:
                if list[root] > list[root * 2 + 1]:
                    list[root], list[root * 2 + 1] = list[root * 2 + 1], list[root]
                
                else:
                    break
                    
            else:
                break
    
    return ans
    
if __name__ == '__main__':
    file = open('Test.dat', 'r')

    numbers = file.read().split()[:20]

    file.close()
    
    numbers = [int(i) for i in numbers]
    
    print(numbers)
    
    print(heapSort(numbers))