def countingSort(list):
    max_number = find_max(list)

    temp = [0] * (max_number + 1)
    
    count(list, temp)
    
    modify(temp)

    return sort(list, temp)
    
def find_max(list):
    max =  list[0]
    
    for i in list:
        if i > max:
            max = i

    return max
    
def count(list, temp):
    for i in list:
        temp[i] = temp[i] + 1
        
def modify(temp):
    for i, d in enumerate(temp):
        if i > 0:
            temp[i] = temp[i - 1] + d
            
def sort(list, temp):
    ans = [0] * len(list)
    
    for i in list:
        ans[temp[i] - 1] = i
        
        temp[i] = temp[i] - 1
        
    return ans
        
if __name__ == '__main__':
    file = open('./Desktop/Test.dat', 'r')

    numbers = file.read().split()[:20]

    file.close()
    
    numbers = [int(i) for i in numbers]
    
    print(numbers)

    print(countingSort(numbers))