def mergeSort(dataList):
    dataList[:] = divide(dataList)

def divide(dataList):
    if len(dataList) < 2:
        return dataList
    
    middle = int(len(dataList) / 2)
    
    left = divide(dataList[:middle])
    
    right = divide(dataList[middle:])
    
    return merge(left, right)
    
def merge(left, right):
    ans = []
    
    while left and right:
        if left[0] <= right[0]:
            ans.append(left.pop(0))
            
        else:
            ans.append(right.pop(0))
            
    if left:
        ans = ans + left
        
    if right:
        ans = ans + right
        
    return ans
