def quicksort(arr,low,high):
    if low >= high:
        return
    else:
        p = partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j] ,arr[i]
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return (i+1)


arr = [-2,3,-1,0,3,10,7,8,4]
n = len(arr)
quicksort(arr,0,n-1)
for i in range(n):
    print(arr[i], end=' ')