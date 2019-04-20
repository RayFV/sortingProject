def mergeSort(list):
    return divide(list)

def divide(list):
    if len(list) < 2:
        return list
    
    middle = int(len(list) / 2)
    
    left = divide(list[:middle])
    
    right = divide(list[middle:])
    
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

if __name__ == '__main__':
    file = open('./Desktop/Test.dat', 'r')

    numbers = file.read().split()[:20]

    file.close()
    
    numbers = [int(i) for i in numbers]
    
    print(numbers)
    
    print(mergeSort(numbers))