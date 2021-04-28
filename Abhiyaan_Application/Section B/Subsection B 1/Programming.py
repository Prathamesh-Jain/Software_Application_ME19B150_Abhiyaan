def findMinSwaps(arr, n) :
    # Array to store count of zeroes
    noOfZeroes = [0] * n
     
    # Count number of zeroes
    # on right side of every one.
    noOfZeroes[0] = 1 - arr[0]
    for i in range(1,n) :
        noOfZeroes[i] = noOfZeroes[i - 1]
        if (arr[i] == 0) :
            noOfZeroes[i] = noOfZeroes[i] + 1
 
    # Count total number of swaps by adding
    # number of zeroes on right side of
    # every one.
    prev = noOfZeroes[0]
    max_count = 0
    count = 0
    idx_end = 0
    lst = []
    if(prev==0):
        lst.append(0)
    for i in range(1,len(noOfZeroes)):
        curr = noOfZeroes[i]
        if(curr == prev):
            count = count + 1
            lst.append(i)
        else:
            count = 0
        if(count>max_count):
            max_count = count
            zeroCount = noOfZeroes[i]
            idx_end = i
        prev = curr
    #print(max_count)
    #print(idx_end)
    #print(noOfZeroes)
    #print(lst)
    swap = 0
    for idx in lst:
        swap = swap + abs(zeroCount - noOfZeroes[idx])
 
    return swap
 
# Driver code
x = int(input('Enter n:'))
arr = list(map(int, input('Enter array seperated by space:').split()))
n = len(arr)
if(n == x):
    print (findMinSwaps(arr, n))
else:
    print('Invalid input!')