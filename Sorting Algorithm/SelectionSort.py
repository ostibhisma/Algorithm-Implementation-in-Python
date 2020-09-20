 def selection(array):
    size = len(array)
    for step in range(size):
        min_index = step
        for i in range(step+1,size):
            if array[i]<array[min_index]:
                min_index = i
        array[step],array[min_index] = array[min_index],array[step]
        print(array)

selection([45,12,9,77,90,109,22,56,92,85,3,99,1,100])