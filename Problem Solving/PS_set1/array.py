def shiftMultiple(arr):
    n = len(arr)
    i = 0
    j = 0
    while(j< n):
        if (arr[j] % 10 == 0):
            j += 1
        else:
            arr[j], arr[i] = arr[i], arr[j]
        
            i += 1
    print(arr)

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i]= int(input())
shiftMultiple(arr)