def linear_search(arr,key):
    for i in range(0,len(arr)):
        if arr[i] == key:
            return i
        else:
            return -1

arr = [3, 4, 5, 6, 7, 8, 9]
result = linear_search(arr, 5)
if(result == -1):
    print("Result not found")
else:
    print("Result found")


# Time Complexity: O(n)

# APPLICATION
# For searching operations in smaller arrays (<100 items).