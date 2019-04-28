def countingSort(list):
    max_number, min_number = find_max_and_min(list)
    
    digit = find_min_digit(list)

    temp = [0] * (max_number * 10 ** digit - min_number * 10 ** digit + 1)
    
    count(list, temp, min_number, digit)
    
    modify(temp)

    return sort(list, temp, min_number, digit)
    
def find_max_and_min(list):
    max = list[0]
    
    min = list[0]
    
    for i in list:
        if i > max:
            max = i

        if i < min:
            min = i
            
    return max, min
    
def find_min_digit(list):
    min_digit = 0

    for i in list:
        x = str(i)
        
        if x.find('.') != -1:
            digit =  len(x) - x.find('.') - 1
    
            if min_digit < digit:
                min_digit = digit
    
    return min_digit
    
def count(list, temp, min_number, digit):
    for i in list:
        temp[int(i * 10 ** digit - min_number * 10 ** digit)] = temp[int(i * 10 ** digit - min_number * 10 ** digit)] + 1
        
def modify(temp):
    for i, d in enumerate(temp):
        if i > 0:
            temp[i] = temp[i - 1] + d
            
def sort(list, temp, min_number, digit):
    ans = [0] * len(list)
    
    for i in list:
        ans[temp[int(i * 10 ** digit - min_number * 10 ** digit)] - 1] = i
        
        temp[int(i * 10 ** digit - min_number * 10 ** digit)] = temp[int(i * 10 ** digit - min_number * 10 ** digit)] - 1
        
    return ans
        
if __name__ == '__main__':
    file = open('Test.dat', 'r')

    numbers = file.read().split()[:20]

    file.close()
    
    numbers = [int(i) for i in numbers]
    numbers = [2, 0, 9, 0, 0.7, 1, -3, 4, 3, 2]
    numbers = [-5, 0, 1, 500, 0.7, 0, -0.002, 3]
    print(numbers)

    print(countingSort(numbers))