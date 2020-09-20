def binary_search(arr,key,low,high):
    n = len(arr)
    if high >= low :
        mid = (low + high) // 2
        if (arr[mid] == key):
            return mid
        elif (key < arr[mid]):
            return binary_search(arr,key,low,mid-1)
        else:
            return binary_search(arr, key, mid+1,high)
    else:
        return -1

arr = [3, 4, 5, 6, 7, 8, 9]
result = binary_search(arr, 7, 0, len(arr)-1)
if(result == -1):
    print("Result not found")
else:
    print("Result found at index " + str(result))


"""
Time Complexities

    Best case complexity: O(1)
    Average case complexity: O(log n)
    Worst case complexity: O(log n)

"""

