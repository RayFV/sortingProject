'''
可以考慮用Linked list代替bucketList，Big-o會從O(K*N) 變成 O(N)
'''

import math

def radixSort(dataList, radix=10):
    K = math.ceil(math.log(max(dataList)+1, radix))
    # print(K)
    for i in range(1, K+1):
        # print(i)
        bucketList = [[] for _ in range(radix)]

        for data in dataList:
            index = data%(radix**i)//(radix**(i-1))
            bucketList[index].append(data)

        dataList.clear()

        for bucket in bucketList:
            dataList += bucket
